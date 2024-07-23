"""
Import HTTP Response and render for
internals
"""
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.models import Cohort, CurrentTasks, User, Project, Tasks, Marks, Events, Servers, Concepts, Sandbox
from .forms import RegistrationForm
# A view No template.

@login_required
def dashboard(request):
    """
    This function handles dashbord request
    """
    try:
        myuser = get_object_or_404(User, user_name=request.user.username)
        current = CurrentTasks.objects.filter(cohort_name=myuser.cohort)
        context = {
        "marks" : Marks.objects.filter(user=myuser),
        "current_tasks" : current,
        "title": "Dashbord",
        }
    except:
        myuser = None
        current = None
        context = {
            "marks": myuser,
            "current_tasks" : current
        }
    
    return render(request, 'dashboard.html', context=context)

@login_required
def profile(request):
    """
    This function handles a profile page request
    """
    return render(request, 'profile.html')

@login_required
def servers(request):

    """
    This function returns the servers that 
    belong to a particular user
    """
    context = {
        "title":"servers",
    }
    try:
        myuser = get_object_or_404(User, user_name=request.user.username)
        sv = Servers.objects.filter(user=myuser)
        context['server'] = sv
    except:
        context['server'] = None
    return render(request, 'servers.html', context=context)

@login_required
def concepts(request):
    """
    This function returns concepts that
    a user has to cover
    """
    context = {
        "title":"concepts",
    }
    try:
        myuser = get_object_or_404(User, user_name=request.user.username)
        user_cohort = myuser.cohort
        concepts = Concepts.objects.filter(cohort=user_cohort)
        context['concepts'] = concepts
    except:
        context['concepts'] = None

    return render(request, "concepts.html", context=context)

@login_required
def sandboxes(request):
    """
    This returns the available
    sandboxes and their details to the user
    """
    context = {
        "title":"sandboxes",
    }
    try:
        myuser = get_object_or_404(User, user_name=request.user.username)
        sb = Sandbox.objects.filter(user=myuser)
        context['sandbox'] = sb
    except:
        context['sandbox'] = None
    return render(request, "sandboxes.html", context=context)

@login_required
def projects(request):
    """
    Fetches the projects and the tasks
    sor far done by a user
    """
    # Get all project
    project = Tasks.objects.all()
    context = {
        'projects' : project,
        'title' : "Projects",
    }
    return render(request, "projects.html", context=context)

def homepage(request):
    return render(request, 'homepage.html', {"title":"homepge"})

@login_required
def tasks(request, project_ID):
    """
    This function fetches tasks in a given
    project
    """
    s_project = Project.objects.get(project_id = project_ID)
    my_tasks = Tasks.objects.filter(project = s_project) # Fetch tasks
    number = my_tasks.count() # Number of tasks
    context = {
        'tasks': my_tasks,
        'title': 'Tasks',
    }
    return render(request, 'tasks.html', context=context)

@login_required
def concept_detail(request, concept_title):
    context = {}
    try:
        concepts = Concepts.objects.get(concept_title=concept_title)
        context['concepts'] = concepts
        context['title'] = concepts.concept_title
    except:
        context['concepts'] = None
    return render(request, 'concept_detail.html', context=context)

def signup(request):
    form = RegistrationForm(request.POST)
    from django.contrib.auth.models import User as usr
    if form.is_valid():
        if not User.objects.filter(user_name=request.POST['user_name']).first():
            form.save()
            my_user = usr.objects.create(username=request.POST['user_name'])
            my_user.set_password('12345')
            my_user.save()
            return redirect(reverse('login'))
    context = {
        "form" : form,
        'title': 'SignUp'
    }
    return render(request, "signup.html", context=context)
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
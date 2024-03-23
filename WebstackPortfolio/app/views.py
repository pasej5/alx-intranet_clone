"""
Import HTTP Response and render for
internals
"""
#from django.http import HttpResponse
from django.shortcuts import render

# A view No template.

def login(request):
    """
    This function handles the login page request
    """
    return render(request, 'login.html')


def dashboard(request):
    """
    This function handles dashbord request
    """
    return render(request, 'dashboard.html')

def profile(request):
    """
    This function handles a profile page request
    """
    return render(request, 'profile.html')

def servers(request):
    """
    This function returns the servers that 
    belong to a particular user
    """
    return render(request, 'servers.html')

def concepts(request):
    """
    This function returns concepts that
    a user has to cover
    """
    return render(request, "concepts.html")

def sandboxes(request):
    """
    This returns the available
    sandboxes and their details to the user
    """
    return render(request, "sandbox.html")

def projects(request):
    """
    Fetches the projects and the tasks
    sor far done by a user
    """
    return render(request, "projects.html")

def tasks(request, project_ID):
    """
    This function fetches tasks in a given
    project
    """
    return render(request, 'tasks.html')
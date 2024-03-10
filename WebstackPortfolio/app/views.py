from django.http import HttpResponse
from django.shortcuts import render

# A view No template.

"""
Context for the login page
"""
def login(request):
    return render(request, 'login.html')


"""
Context for the dashboard
"""
def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')
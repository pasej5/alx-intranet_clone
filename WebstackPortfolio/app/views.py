from django.http import HttpResponse
from django.shortcuts import render

# A view No template.
def login(request):
    return render(request, 'login.html')
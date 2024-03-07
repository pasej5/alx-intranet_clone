from django.http import HttpResponse
from django.shortcuts import render

# A view No template.
def home(request):
    return HttpResponse("hello Word")
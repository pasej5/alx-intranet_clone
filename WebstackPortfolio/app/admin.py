from django.contrib import admin
from app.models import Cohort, CurrentTasks, User, Project, Tasks, Marks, Events, Servers, Concepts, Sandbox
# Register your models here.
my_models = [Cohort, CurrentTasks, User, Project, Tasks, Marks, Events, Servers, Concepts, Sandbox]
admin.site.register(my_models)
from django.urls import path

from .import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('concepts/', views.concepts, name='concepts'),
    path('sandboxes/', views.sandboxes, name='sandboxes'),
    path('servers/', views.servers, name='servers'),
    path('tasks/<int:project_ID>', views.tasks, name='tasks'),
    path('homepage/', views.homepage, name='homepage'),
    path('sandboxes', views.sandboxes, name='sandboxes')
]

"""
Import django database module
"""
from django.db import models

# User model
class User(models.Model):
    """
    This is the user table, it contains details
    about our users.
    """
    gender_choices = (
        ("MALE", "male"),
        ("FEMALE", "female")
        )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_gender = models.CharField(max_length=1)
    user_id = models.IntegerField()
    user_status = models.CharField(max_length=10, choices=gender_choices)
    cohort_id = models.IntegerField()
    date_registered = models.DateField()
    user_discord = models.CharField(max_length=100)

class Projects(models.Model):
    """
    This entity contains all projects to be done
    by the users.
    """
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=100)
    cohort_id = models.IntegerField()

class Tasks(models.Model):
    """
    This entity defines records containing
    tasks.
    Each task should have a project ID to 
    which it belong
    """
    project_id = models.IntegerField()
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=100)

class Cohort(models.Model):
    """
    This is the cohort entity
    It stores user cohorts
    """
    cohort_id = models.IntegerField()
    cohort_name = models.CharField(max_length=3)

class Marks(models.Model):
    """
    This table stores all marks of users
    using the system
    """
    user_id = models.IntegerField()
    task_id = models.IntegerField()
    project_id = models.IntegerField()
    mark = models.IntegerField()
    month_id = models.IntegerField()

class Events(models.Model):
    """
    This entity stores all events users can attend
    to.
    """
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=100)
    event_time = models.TimeField()
    event_date = models.DateField()
    event_url = models.CharField(max_length=150)

class Servers(models.Model):
    """
    This entity contains servers of users
    of our system.
    """
    user_id = models.IntegerField()
    server_user_name = models.CharField(max_length=100)
    server_ip = models.CharField(max_length=15)

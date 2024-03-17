"""
Import django database module
"""
from django.db import models

# Create your models here.

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
    user_status = models.CharField(choices=gender_choices)
    cohort_id = models.IntegerField()
    date_registered = models.DateField()
    user_discord = models.CharField(max_length=100)

class projects(models.Model):
    pass

class tasks(models.Model):
    pass

class cohort(models.Model):
    pass

class marks(models.Model):
    pass

class events(models.Model):
    pass

class servers(models.Model):
    pass

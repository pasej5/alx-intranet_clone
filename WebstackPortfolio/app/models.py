"""
Import django database module
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# User model
class Cohort(models.Model):
    """
    This is the cohort entity
    It stores user cohorts
    """
    cohort_name = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.cohort_name}"


class User(models.Model):
    """
    This is the user table, it contains details
    about our users.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_gender = models.CharField(max_length=1)
    user_status = models.CharField(max_length=6)
    cohort = models.ForeignKey(Cohort, default=None, on_delete=models.PROTECT)
    date_registered = models.DateField()
    user_discord = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    """
    This entity contains all projects to be done
    by the users.
    """
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=100)
    cohort = models.ForeignKey(Cohort, default=None, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.project_name}"

class Tasks(models.Model):
    """
    This entity defines records containing
    tasks.
    Each task should have a project ID to 
    which it belong
    """
    project = models.ForeignKey(Project, default=None, on_delete=models.PROTECT)
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=100)
    task_content = models.TextField(max_length=5000)
    task_requirements = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.task_name}"

class Marks(models.Model):
    """
    This table stores all marks of users
    using the system
    """
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    task = models.ForeignKey(Tasks, default=None, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, default=None, on_delete=models.PROTECT)
    mark = models.IntegerField()
    """
    To save server space and resouces the user will be
    required to host their work on third party apps like github
    So they share the URL which is saved here
    """
    solution_url = models.CharField(default=None, max_length=200)
    month_id = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)])

    def __str__(self) -> str:
        return f"{self.month_id} {self.mark}"

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

    def __str__(self) -> str:
        return f"{self.event_name} {self.event_time}"

class Servers(models.Model):
    """
    This entity contains servers of users
    of our system.
    """
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    server_user_name = models.CharField(max_length=100)
    server_ip = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.server_user_name} {self.server_ip}"

class Concepts(models.Model):
    """
    This entity handles concepts that are
    to be covered by a all users of a given cohort
    """
    cohort = models.ForeignKey(Cohort, default=None, on_delete=models.PROTECT)
    concept_title = models.CharField(max_length=100)
    concept_content = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return f"{self.concept_title}"

class Sandbox(models.Model):
    """
    This stores sandboxes given to the user by
    admins.
    """
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    sandbox_name = models.CharField(max_length=30)
    sandbox_detail = models.CharField(max_length=30)
    sandbox_url = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.sandbox_name}"

 
class CurrentTasks(models.Model):
    """
        This model issue a task command center for all cohorts.
    """
    day = models.IntegerField()
    month = models.IntegerField()
    cohort_name = models.ForeignKey(Cohort, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, default=None, on_delete=models.PROTECT)

class PeerLearning(models.Model):
    date = models.DateField()
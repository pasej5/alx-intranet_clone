from django.utils import timezone
from app.models import Cohort, User, Project, Tasks, Marks, Events, Servers, Concepts, Sandbox

# Create a cohort
cohort1 = Cohort.objects.create(cohort_name='C1')

# Create a user
user1 = User.objects.create(
    first_name='John',
    last_name='Doe',
    user_name='johndoe',
    user_gender='M',
    user_status='ACTIVE',
    cohort=cohort1,
    date_registered=timezone.now(),
    user_discord='johndoe#1234',
    github_username='johndoe'
)

# Create a project
project1 = Project.objects.create(
    project_id=1,
    project_name='Project 1',
    cohort=cohort1
)

# Create a task
task1 = Tasks.objects.create(
    project=project1,
    task_id=1,
    task_name='Task 1',
    task_content='This is task 1',
    task_requirements='These are the requirements for task 1'
)

# Create a mark
mark1 = Marks.objects.create(
    user=user1,
    task=task1,
    project=project1,
    mark=85,
    solution_url='https://github.com/johndoe/project1',
    month_id=1
)

# Create an event
event1 = Events.objects.create(
    event_id=1,
    event_name='Event 1',
    event_time=timezone.now().time(),
    event_date=timezone.now().date(),
    event_url='https://event1.com'
)

# Create a server
server1 = Servers.objects.create(
    user=user1,
    server_user_name='johndoe',
    server_ip='192.168.1.1'
)

# Create a concept
concept1 = Concepts.objects.create(
    cohort=cohort1,
    concept_title='Concept 1',
    concept_content='This is concept 1'
)

# Create a sandbox
sandbox1 = Sandbox.objects.create(
    user=user1,
    sandbox_name='Sandbox 1',
    sandbox_detail='This is sandbox 1',
    sandbox_url='https://sandbox1.com'
)

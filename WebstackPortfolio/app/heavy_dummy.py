from django.utils import timezone
from app.models import Cohort, User, Project, Concepts, Tasks, Marks, Events, Servers, Sandbox, CurrentTasks

# Create cohorts
cohorts = ['A1', 'B2', 'C3']
for name in cohorts:
    cohort = Cohort(cohort_name=name)
    cohort.save()
# Create users
first_names = ['John', 'Jane', 'Jim']
last_names = ['Doe', 'Smith', 'Johnson']
user_names = ['johndoe', 'janesmith', 'jimjohnson']
genders = ['M', 'F', 'M']
statuses = ['Active', 'Inactive', 'Active']
cohorts = Cohort.objects.all()
for i in range(3):
    user = User(
        first_name=first_names[i],
        last_name=last_names[i],
        user_name=user_names[i],
        user_gender=genders[i],
        user_status=statuses[i],
        cohort=cohorts[i],
        date_registered=timezone.now(),
        user_discord=f'{user_names[i]}#1234',
        github_username=user_names[i]
    )
    user.save()
# Create projects
project_names = ['Project 1', 'Project 2', 'Project 3']
for i in range(3):
    project = Project(project_id=i+1, project_name=project_names[i], cohort=cohorts[i])
    project.save()
# Create concepts
concept_titles = ['Concept 1', 'Concept 2', 'Concept 3']
concept_contents = ['This is concept 1', 'This is concept 2', 'This is concept 3']
for i in range(3):
    concept = Concepts(id=i+1, cohort=cohorts[i], concept_title=concept_titles[i], concept_content=concept_contents[i])
    concept.save()
# Create tasks
task_names = ['Task 1', 'Task 2', 'Task 3']
task_contents = ['This is task 1', 'This is task 2', 'This is task 3']
task_requirements = ['Requirement 1', 'Requirement 2', 'Requirement 3']
projects = Project.objects.all()
concepts = Concepts.objects.all()
for i in range(3):
    task = Tasks(project=projects[i], task_id=i+1, task_name=task_names[i], task_content=task_contents[i], task_requirements=task_requirements[i], concept=concepts[i])
    task.save()
# Create marks
marks = [85, 90, 95]
users = User.objects.all()
tasks = Tasks.objects.all()
for i in range(3):
    mark = Marks(user=users[i], task=tasks[i], project=projects[i], mark=marks[i], solution_url=f'https://github.com/{user_names[i]}/project{i+1}', month_id=1)
    mark.save()
# Create even
event_names = ['Event 1', 'Event 2', 'Event 3']
for i in range(3):
    event = Events(event_id=i+1, event_name=event_names[i], event_time=timezone.now(), event_date=timezone.now().date(), event_url=f'https://event{i+1}.com')
    event.save()
# Create servers
server_ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
for i in range(3):
    server = Servers(user=users[i], server_user_name=user_names[i], server_ip=server_ips[i])
    server.save()
# Create sandboxes
sandbox_names = ['Sandbox 1', 'Sandbox 2', 'Sandbox 3']
sandbox_details = ['Detail 1', 'Detail 2', 'Detail 3']
for i in range(3):
    sandbox = Sandbox(user=users[i], sandbox_name=sandbox_names[i], sandbox_detail=sandbox_details[i], sandbox_url=f'https://sandbox{i+1}.com')
    sandbox.save()
# Create current tasks
for i in range(3):
    current_task = CurrentTasks(day=1, month=1, cohort_name=cohorts[i], project=projects[i])
    current_task.save()
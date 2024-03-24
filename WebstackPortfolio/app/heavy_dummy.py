from django.utils import timezone
from app.models import Cohort, User, Project, Tasks, Marks, Events, Servers, Concepts, Sandbox
import random
from random import choice
"""
Create cohorts (9 cohorts)
"""
for i in range(1, 10):
    # Create cohorts
    cohort = Cohort.objects.create(cohort_name=f'C{i}')
    cohort.save()
"""
Create projects (99 projects)
"""
for i in range(1, 100):
    cohortid = random.randint(1, 9)
    # Get cohorts
    cohort = Cohort.objects.get(cohort_name=f'C{cohortid}')
    project = Project.objects.create(
        project_id=i,
        project_name=f'Project {i}',
        cohort=cohort
    )
    # Create tasks and each task has a concept
    for i in range(1, 7):
        # Create concepts
        concept = Concepts.objects.create(
        cohort=cohort,
        concept_title=f'Concept {i}',
        concept_content=f'This is concept {i}'
        )
        # Create the task
        rand = random.randint(1, 10000)
        task = Tasks.objects.create(
            project=project,
            task_id=rand,
            task_name=f'Task {rand}',
            task_content=f'This is task {rand}',
            task_requirements=f'These are the requirements for task {rand}'
        )
for i in range(1, 50):
    #Assign a random cohort to a user
    cohortid = random.randint(1, 9)
    # Get cohorts
    cohort = Cohort.objects.get(cohort_name=f'C{cohortid}')
    #Assign a random mark to a student
    #mark = random.randint(60, 200)
    # Create users
    activity = ["Active", "Domant"]
    idx = random.randint(0, 1)
    user = User.objects.create(
        first_name=f'User{i}',
        last_name=f'Doe{i}',
        user_name=f'userdoe{i}',
        user_gender='M',
        user_status=activity[idx],
        cohort=cohort,
        date_registered=timezone.now(),
        user_discord=f'userdoe{i}#1234',
        github_username=f'userdoe{i}'
    )
    user.save()
    # Create servers
    ser = random.randint(1, 9)
    server = Servers.objects.create(
        user=user,
        server_user_name=f'userdoe{i}',
        server_ip=f'1{i+ser}2.168.1.{i}'
    )
    server.save()
    # Create sandboxes
    sandbox = Sandbox.objects.create(
        user=user,
        sandbox_name=f'Sandbox {i}',
        sandbox_detail=f'This is sandbox {i}',
        sandbox_url=f'https://sandbox{i}.com'
    )
    sandbox.save()
# Create events
for i in range(1, 50):
    event = Events.objects.create(
        event_id=i,
        event_name=f'Event {i}',
        event_time=timezone.now().time(),
        event_date=timezone.now().date(),
        event_url=f'https://event{i}.com'
    )
    event.save()
# Create random marks for students
for j in range(1, 50):
    for i in range(0, 11):
        mark = random.randint(60, 200)
        # Get random task
        pks = Tasks.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        task = Tasks.objects.get(pk=random_pk)
        #Catch a bug
        try:
            myuser=User.objects.get(first_name=f'User{j}')
            # create mark
            mark = Marks.objects.create(
                user=myuser,
                task=task,
                project=task.project,
                mark=mark,
                solution_url=f'https://github.com/userdoe{j}/project{i}/{task.task_name}',
                month_id=i
            )
            mark.save()
        except:
            print(f'User{j} is not found')
            j += 1
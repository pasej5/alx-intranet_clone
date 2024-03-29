from django.test import TestCase

from django.test import TestCase
from .models import Cohort, User, Project, Concepts, Tasks, Marks, Events, Servers, Sandbox, CurrentTasks

class ModelTestCase(TestCase):
    def setUp(self):
        self.cohort = Cohort.objects.create(cohort_name="TestCohort")
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            user_name="johndoe",
            user_gender="M",
            user_status="Active",
            cohort=self.cohort,
            date_registered="2024-01-01",
            user_discord="johndoe#1234",
            github_username="johndoe123"
        )
        self.project = Project.objects.create(
            project_id=1,
            project_name="TestProject",
            cohort=self.cohort
        )
        self.concepts = Concepts.objects.create(
            id=1,
            cohort=self.cohort,
            concept_title="TestConcept",
            concept_content="TestContent"
        )
        self.tasks = Tasks.objects.create(
            project=self.project,
            task_id=1,
            task_name="TestTask",
            task_content="TestContent",
            task_requirements="TestRequirements",
            concept=self.concepts
        )
        self.marks = Marks.objects.create(
            user=self.user,
            task=self.tasks,
            project=self.project,
            mark=80,
            solution_url="http://example.com",
            month_id=1
        )
        self.events = Events.objects.create(
            event_id=1,
            event_name="TestEvent",
            event_time="12:00:00",
            event_date="2024-01-01",
            event_url="http://example.com"
        )
        self.servers = Servers.objects.create(
            user=self.user,
            server_user_name="TestUser",
            server_ip="127.0.0.1"
        )
        self.sandbox = Sandbox.objects.create(
            user=self.user,
            sandbox_name="TestSandbox",
            sandbox_detail="TestDetail",
            sandbox_url="http://example.com"
        )
        self.current_tasks = CurrentTasks.objects.create(
            day=1,
            month=1,
            cohort_name=self.cohort,
            project=self.project
        )

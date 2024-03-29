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
    def test_cohort_model(self):
        self.assertEqual(str(self.cohort), "TestCohort")
        
    def test_user_model(self):
        self.assertEqual(str(self.user), "John Doe")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
    
    def test_project_model(self):
        self.assertEqual(str(self.project), "TestProject")
        self.assertEqual(self.project.project_id, 1)
    
    def test_concepts_model(self):
        self.assertEqual(str(self.concepts), "TestConcept")
        self.assertEqual(self.concepts.id, 1)
        
    def test_tasks_model(self):
        self.assertEqual(str(self.tasks), "TestTask")
        self.assertEqual(self.tasks.task_id, 1)
        
    def test_marks_model(self):
        self.assertEqual(str(self.marks), "1 80")
        self.assertEqual(self.marks.mark, 80)
    
    def test_events_model(self):
        self.assertEqual(str(self.events), "TestEvent 12:00:00")
        self.assertEqual(self.events.event_id, 1)
        
    def test_servers_model(self):
        self.assertEqual(str(self.servers), "TestUser 127.0.0.1")
        
    def test_current_tasks_model(self):
        self.assertEqual(self.current_tasks.day, 1)
        self.assertEqual(self.current_tasks.month, 1)
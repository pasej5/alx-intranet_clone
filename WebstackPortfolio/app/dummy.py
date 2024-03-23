import models


cohorts = {
    "cohort 13" : models.Cohort(cohort_name="C13"),
    "cohort 12" : models.Cohort(cohort_name="C12"),
    "cohort 11" : models.Cohort(cohort_name="C11")
        }

users = {
    "first_user" : models.User(
        first_name="Namwamba",
        last_name="Marvin",
        user_name="shantmarvis",
        user_gender="male",
        user_status="Active",
        cohort=cohorts["cohort 13"],
        date_registered="2023-01-01",
        user_discord="marvin.2002",
        github_username="NamwambaMarvin",
        ),
    "first_user" : models.User(
        first_name="Nalweyiso",
        last_name="Mary",
        user_name="NalMary",
        user_gender="female",
        user_status="Active",
        cohort=cohorts["cohort 12"],
        date_registered="2023-03-24",
        user_discord="NalweyisoMary",
        github_username="NalweyisoMary"
        )
}

projects = {
    "project_name" : models.Project(
        project_id=1001,
        project_name="Python",
        cohort=cohorts["cohort 13"]
    )
}

tasks = {
    "task1": models.Project(
        project=projects["project_name"],
        task_id=1,
        task_name="Introduction to python",
        task_content="Hello from python",
        task_requirements="Install emacs and python on your system",
    )
}

marks = [

    models.Marks(
        user=,
        task=,
        project=,
        mark=,
        solution_url=,
        month_id=,
    ),
]
events = [
    models.Events(
        event_id=,
        event_name=,
        event_time=,
        event_date=,
        event_url=,

    )
]

concepts = [
    models.Concepts(
        cohort=,
        concept_title=,
        concept_content=,
    )
]

sandbox = [
    models.Sandbox(
        user=,
        sandbox_name=,
        sandbox_detail=,
        sandbox_url=,
    )
]

servers = [
    models.Servers(
        user=,
        server_user_name=,
        server_ip=,
    ),
]
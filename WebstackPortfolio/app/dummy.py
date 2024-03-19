import models

cohorts = {
    "cohort 13" : models.Cohort(cohort_name="C13"),
    "cohort 12" : models.Cohort(cohort_name="C12"),
    "cohort 11" : models.Cohort(cohort_name="C11")
           }
users = {
    "first_user" : models.User(
        first_name=,
        last_name=,
        user_name=,
        user_gender=,
        user_status=,
        cohort=,
        date_registered=,
        user_discord=,
        ),
    "first_user" : models.User(
        first_name=,
        last_name=,
        user_name=,
        user_gender=,
        user_status=,
        cohort=,
        date_registered=,
        user_discord=,
        ),
    "first_user" : models.User(
        first_name=,
        last_name=,
        user_name=,
        user_gender=,
        user_status=,
        cohort=,
        date_registered=,
        user_discord=,
        ),
    "first_user" : models.User(
        first_name=,
        last_name=,
        user_name=,
        user_gender=,
        user_status=,
        cohort=,
        date_registered=,
        user_discord=,
        ),
    "first_user" : models.User(
        first_name=,
        last_name=,
        user_name=,
        user_gender=,
        user_status=,
        cohort=,
        date_registered=,
        user_discord=,
        ),
}

projects = {
    "project_name" : models.Project(
        project_id=,
        project_name=,
        cohort=,
    )
}

tasks = {
    "task1": models.Project(
        project=,
        task_id=,
        task_name=,
        task_content=,
        task_requirements=,
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
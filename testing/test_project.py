from models.project import Project

def test_project_creation():

    project = Project(
        1,
        "CLI Tool",
        "Project App",
        "2026-12-31"
    )

    assert project.owner_id == 1
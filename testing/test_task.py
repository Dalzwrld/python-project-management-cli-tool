from models.task import Task

def test_task_completion():

    task = Task(
        1,
        "Build CLI",
        "Alex"
    )

    task.mark_complete()

    assert task.status == "Completed"
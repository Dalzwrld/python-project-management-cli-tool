import argparse

from rich.console import Console
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task

from utils.storage import load_data, save_data

console = Console()

def add_user(args):
    data = load_data()
    
    if data["users"]:
        next_id = max(
            user["id"]
            for user in data["users"]
        ) + 1
    else:
        next_id = 1

    user = User(
        args.name,
        args.email,
        next_id
    )

    data["users"].append(user.to_dict())

    save_data(data)

    console.print("[green]User added successfully[/green]")


def list_users(args):

    data = load_data()

    table = Table(title="Users")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for user in data["users"]:
        table.add_row(
            str(user["id"]),
            user["name"],
            user["email"]
        )

    console.print(table)


def add_project(args):

    data = load_data()

    if data["projects"]:
        next_id = max(
            project["id"]
            for project in data["projects"]
        ) + 1
    else:
        next_id = 1

    project = Project(
        args.user_id,
        args.title,
        args.description,
        args.due_date,
        next_id
    )

    data["projects"].append(project.to_dict())

    save_data(data)

    console.print("[green]Project added[/green]")


def list_projects(args):

    data = load_data()

    table = Table(title="Projects")

    table.add_column("ID")
    table.add_column("Owner ID")
    table.add_column("Title")
    table.add_column("Due Date")

    projects = data["projects"]

    if args.user_id:
        projects = [
            p for p in projects
            if p["owner_id"] == args.user_id
        ]

    for project in projects:
        table.add_row(
            str(project["id"]),
            str(project["owner_id"]),
            project["title"],
            project["due_date"]
        )

    console.print(table)


def add_task(args):

    data = load_data()

    if data["tasks"]:
        next_id = max(
            task["id"]
            for task in data["tasks"]
        ) + 1
    else:
        next_id = 1

    task = Task(
        args.project_id,
        args.title,
        args.assigned_to,
        "Pending",
        next_id
    )

    data["tasks"].append(task.to_dict())

    save_data(data)

    console.print("[green]Task added[/green]")


def list_tasks(args):

    data = load_data()

    table = Table(title="Tasks")

    table.add_column("ID")
    table.add_column("Project")
    table.add_column("Title")
    table.add_column("Assigned To")
    table.add_column("Status")

    for task in data["tasks"]:
        table.add_row(
            str(task["id"]),
            str(task["project_id"]),
            task["title"],
            task["assigned_to"],
            task["status"]
        )

    console.print(table)


def complete_task(args):

    data = load_data()

    for task in data["tasks"]:
        if task["id"] == args.task_id:
            task["status"] = "Completed"

            save_data(data)

            console.print(
                "[green]Task completed[/green]"
            )
            return

    console.print("[red]Task not found[/red]")


def delete_task(args):

    data = load_data()

    data["tasks"] = [
        t for t in data["tasks"]
        if t["id"] != args.task_id
    ]

    save_data(data)

    console.print("[yellow]Task deleted[/yellow]")


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)


    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user-id", type=int, required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", required=True)
    add_project_parser.set_defaults(func=add_project)

    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user-id", type=int)
    list_projects_parser.set_defaults(func=list_projects)


    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project-id", type=int, required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", required=True)
    add_task_parser.set_defaults(func=add_task)

    list_tasks_parser = subparsers.add_parser("list-tasks")
    list_tasks_parser.set_defaults(func=list_tasks)

    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--task-id", type=int, required=True)
    complete_task_parser.set_defaults(func=complete_task)

    delete_task_parser = subparsers.add_parser("delete-task")
    delete_task_parser.add_argument("--task-id", type=int, required=True)
    delete_task_parser.set_defaults(func=delete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
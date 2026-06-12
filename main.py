import argparse

from rich.console import Console
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task

from utils.storage import load_data, save_data

console = Console

def add_user(args):
    data = load_data()
    user = User(args.name, args.email)

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

    user_exists = any(
        user["id"] == args.user_id
        for user in data["users"]
    )

    if not user_exists:
        console.print("[red]User not found[/red]")
        return

    project = Project(
        args.user_id,
        args.title,
        args.description,
        args.due_date
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


parse = argparse.ArgumentParser(
    description="Project Management CLI"
)

subparsers = parse.add_subparsers(dest="command")


add_user = subparsers.add_parser("add_user")

add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)


add_project = subparsers.add_parser("add_project")

add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)


add_task = subparsers.add_parser("add_task")

add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)
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
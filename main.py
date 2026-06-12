import argparse

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
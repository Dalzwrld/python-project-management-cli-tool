import argparse

parse = argparse.ArgumentParser(
    description="Project Management CLI"
)

subparsers = parse.add_subparsers(dest="command")

add_user = subparsers.add_parser("add_user")

add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)
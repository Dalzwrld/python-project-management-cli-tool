import argparse

parse = argparse.ArgumentParser(
    description="Project Management CLI"
)

subparsers = parse.add_subparsers(dest="command")
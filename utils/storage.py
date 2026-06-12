import json
import os

data_file = "data/data.json"

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    if not os.path.exists(data_file):
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }
    
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }
    
def get_next_id(items):

    if not items:
        return 1

    return max(
        item["id"]
        for item in items
    ) + 1
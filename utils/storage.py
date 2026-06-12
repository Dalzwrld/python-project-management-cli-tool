import json
import os

data_file = "data/data.json"

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
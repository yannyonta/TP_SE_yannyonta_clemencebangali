import json

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

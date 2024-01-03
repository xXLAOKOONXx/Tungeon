import json

from tungeon.data.company import Company


def save(company:Company, file_path:str):
    with open(file_path, 'w') as f:
        json.dump(company.__dict__(), f)

def load(file_path:str) -> Company:
    with open(file_path, 'r') as f:
        json_dict = json.load(f)
    return Company.from_json(json_dict)
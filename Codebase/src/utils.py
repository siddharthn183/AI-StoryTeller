import json
import re

def clean_json(text: str):
    text = text.strip()
    text = re.sub(r"```json|```", "", text)
    text = text.replace("\n", " ")
    return text

def load_metadata(path="data/data.json"):
    with open(path, "r") as f:
        return json.load(f)

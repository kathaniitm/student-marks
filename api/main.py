# # main.py
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

import json
import os
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Path to JSON file in the root directory
json_file_path = os.path.join(os.path.dirname(__file__), "../q-vercel-python.json")

# Function to load JSON data
def load_json_data():
    try:
        with open(json_file_path, "r") as file:
            return json.load(file)  # Load as a list of dictionaries
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    """Fetch marks for given names from JSON file"""
    data = load_json_data()
    
    # Convert list of dictionaries into a lookup dictionary for quick search
    name_to_marks = {entry["name"]: entry["marks"] for entry in data}

    # Retrieve marks in the requested order
    result = [name_to_marks.get(n, 0) for n in name]

    return {"marks": result}

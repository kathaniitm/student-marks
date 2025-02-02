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

# Define the path to the JSON file in the root directory
json_file_path = os.path.join(os.path.dirname(__file__), "../q-vercel-python.json")

# Function to load the JSON file
def load_json_data():
    try:
        with open(json_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file is not found

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    """Fetch marks for given names from q-vercel-python.json"""
    marks_data = load_json_data()
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}

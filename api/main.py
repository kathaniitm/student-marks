# # main.py
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

import json
import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Allow a specific domain
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
    allow_headers=["*"],  # Allow all headers
)

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
def get_marks(name: Optional[List[str]] = Query(default=None)):
    """Fetch marks for given names, or return all if no names are provided"""
    data = load_json_data()
    
    if not name:  
        # No names were provided, return all data
        return {"marks": data}
    
    # Convert list of dictionaries into a lookup dictionary for fast search
    name_to_marks = {entry["name"]: entry["marks"] for entry in data}

    # Retrieve marks in the requested order
    result = [{"name": n, "marks": name_to_marks.get(n, 0)} for n in name]

    return {"marks": result}

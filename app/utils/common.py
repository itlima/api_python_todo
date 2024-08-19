import json
from fastapi import HTTPException


def read_json_file(path: str) -> dict:
    try:
        with open(path) as json_data:
            return json.load(json_data)
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="File not found.")
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Error decoding JSON.")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading file: {str(e)}")

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import json

from pymongo.collection import Collection
from pymongo import MongoClient


app = FastAPI()
templates = Jinja2Templates(directory="templates")

client = MongoClient("mongodb://admin:admin_password@localhost:27017")
db = client["mydatabase"]
collection: Collection = db["mycollection"]


def get_last_numeric() -> int:
    try:
        last_item = collection.find_one(
            sort=[("numeric", -1)]
        )
        return 1 if last_item is None else int(last_item["numeric"]) + 1
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching last numeric value: {str(e)}")


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


def prepare_todo_import(todos: dict, start_numeric: int) -> list:
    todo_prepared_to_import = []
    numeric = start_numeric

    for todo in todos.values():
        todo_prepared_to_import.append({
            "numeric": numeric,
            "task_message": todo
        })
        numeric += 1

    return todo_prepared_to_import

    collection.insert_many(todo_prepared_to_import)
    total_lines = len(todo_prepared_to_import)
    return RedirectResponse("/", 303)


@app.get("/")
async def root(request: Request):

    all_todos = collection.find()
    result_list = list(all_todos)
    response = {
        'content': result_list,
        'size': len(result_list),
    }

    return templates.TemplateResponse("todolist.html", {"request": request, "tododict": response})


@app.get("/delete/{id}")
async def delete_todo(request: Request, id: str):
    print(id)

    result = collection.delete_one({"numeric": int(id)})

    collection.delete_one(
        {
            "numeric": id,
        }
    )

    return RedirectResponse("/", 303)


@app.post("/add")
async def add_todo(request: Request):
    teste = await request.form()

    numeric = get_last_numeric()
    new_document = {
        "numeric": str(numeric),
        "task_message": teste["newtodo"]
    }
    collection.insert_one(new_document)

    return RedirectResponse("/", 303)

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


def get_last_numeric():
    last_item = collection.find_one(sort=[("numeric", -1)])
    new_numeric = 1 if last_item is None else int(last_item["numeric"]) + 1
    return new_numeric


def read_file(path):
    with open(path) as json_data:
        content_file = json.load(json_data)
    return content_file


@app.post("/migrate")
def migrate_todos():

    todos_to_import = read_file('database.json')

    todo_prepared_to_import = []

    numeric = get_last_numeric()
    for todo in todos_to_import:
        data_prepared = {
            "numeric": numeric,
            "task_message": todos_to_import[todo]
        }
        numeric += 1

        todo_prepared_to_import.append(data_prepared)

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

from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo.collection import Collection
from app.db.connection import db
from app.utils.common import read_json_file

templates = Jinja2Templates(directory="templates")
collection: Collection = db["mycollection"]


def fetch_next_numeric_value() -> int:
    try:
        last_item = collection.find_one(
            sort=[("numeric", -1)]
        )
        return 1 if last_item is None else int(last_item["numeric"]) + 1
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching last numeric value: {str(e)}")


def format_todos_for_import(todos: dict, start_numeric: int) -> list:
    todo_prepared_to_import = []
    numeric = start_numeric

    for todo in todos.values():
        todo_prepared_to_import.append({
            "numeric": int(numeric),
            "task_message": todo
        })
        numeric += 1

    return todo_prepared_to_import


async def import_todos():
    todos_to_import = read_json_file('database.json')
    start_numeric = fetch_next_numeric_value()

    todo_prepared_to_import = format_todos_for_import(
        todos_to_import, start_numeric)

    try:
        collection.insert_many(todo_prepared_to_import)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error inserting documents: {str(e)}")

    return RedirectResponse("/", 303)


async def display_todo_list(request: Request):
    try:
        all_todos = list(collection.find())
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching todos: {str(e)}")

    response = {
        'content': all_todos,
        'size': len(all_todos),
    }

    return templates.TemplateResponse("todolist.html", {"request": request, "tododict": response})


async def remove_todo(id: str):
    try:
        result = collection.delete_one({"numeric": int(id)})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404, detail=f"No document found with numeric value {id}.")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid numeric value.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error deleting document: {str(e)}")

    return RedirectResponse("/", 303)


async def create_todo(request: Request):
    try:
        form_data = await request.form()
        task_message = form_data.get("newtodo")
        if not task_message:
            raise HTTPException(
                status_code=400, detail="Task message is required.")

        numeric = fetch_next_numeric_value()
        new_document = {
            "numeric": int(numeric),
            "task_message": task_message
        }

        collection.insert_one(new_document)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error adding new todo: {str(e)}")

    return RedirectResponse("/", 303)


async def update_todo(numeric, content):

    result = collection.update_one({"numeric": int(id)})

    collection.update_one(
        {"numeric": numeric},
        {"$set": {"task_message": content}}
    )
    print(result)

    return RedirectResponse("/", 303)

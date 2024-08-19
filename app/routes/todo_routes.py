from fastapi import APIRouter, Request
from app.services.todo_service import display_todo_list, import_todos, remove_todo, create_todo
router = APIRouter()


@router.get("/")
async def get_todo_list(request: Request):
    return await display_todo_list(request)


@router.post("/migrate")
async def import_todos_from_file():
    return await import_todos()


@router.get("/delete/{numeric}")
async def delete_todo_by_numeric(request: Request, numeric: str):
    return await remove_todo(numeric)


@router.post("/add")
async def add_new_todo(request: Request):
    return await create_todo(request)

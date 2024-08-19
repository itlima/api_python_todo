from fastapi import FastAPI
from app.routes import todo_routes


async def lifespan(app: FastAPI):
    print("Application startup")

    try:
        yield
    finally:

        print("Application shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(todo_routes.router)

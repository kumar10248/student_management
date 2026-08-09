from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.mongodb import client
from app.routes.students import router as student_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting...")

    client.admin.command("ping")
    print("MongoDB connected!")

    yield

    print("Application shutting down...")
    client.close()
    print("MongoDB connection closed!")


app = FastAPI(lifespan=lifespan)
@app.get("/")
def home():
    return{
        "message":"Welcome to student managment"
    }

app.include_router(student_router)
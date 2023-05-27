from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import root, new_releases


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server received the first request!")
    yield
    print("Server received SIGTERM signal.")

app = FastAPI(
    lifespan=lifespan
)

app.include_router(new_releases.router)
app.include_router(root.router)

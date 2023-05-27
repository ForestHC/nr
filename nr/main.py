from contextlib import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime
from .utils import git_info
from .routers import root, new_releases

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server received the first request!")

    app.start_time=datetime.utcnow()
    app.version=git_info.get_tag_or_branch()
    app.commit=git_info.get_revision()
    app.dirty=git_info.get_dirty()

    yield

    print("Server received SIGTERM signal.")

app = FastAPI(
    lifespan=lifespan
)

app.include_router(new_releases.router)
app.include_router(root.router)

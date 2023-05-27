from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from .utils import git_info
from .routers import root, new_releases

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("start server...")

    app.start_time=datetime.utcnow()
    app.version=git_info.get_tag_or_branch()
    app.commit=git_info.get_revision()
    app.dirty=git_info.get_dirty()

    yield

    print("shutdown...")

app = FastAPI(
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(new_releases.router)
app.include_router(root.router)

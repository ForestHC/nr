from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/ping")
def ping():
    return {"ping": "pong"}

@router.get("/version")
def version(request: Request):
    return {
        "version": request.app.version,
        "commit": request.app.commit,
        "start_time": request.app.start_time,
        "dirty": request.app.dirty
    }

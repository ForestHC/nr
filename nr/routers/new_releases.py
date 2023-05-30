from fastapi import APIRouter, Header, HTTPException, Response, status
from typing import Annotated, List
from zoneinfo import ZoneInfo
from dateutil import parser
from ..channel.client import ChannelOpenApiClient
from ..channel.message import Block, Message
from ..schemas.releasehook import ReleaseHook
from ..utils.new_releases import verify_signature


router = APIRouter(
    prefix="/nr",
)


@router.post("/hook", status_code=status.HTTP_201_CREATED)
def hook(
    x_newreleases_signature: Annotated[str, Header()],
    x_newreleases_timestamp: Annotated[str, Header()],
    release: ReleaseHook
) -> Response:
    if not verify_signature(x_newreleases_signature, x_newreleases_timestamp, release):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    release_time = parser.parse(release.time) \
        .astimezone(tz=ZoneInfo('Asia/Seoul'))

    blocks: List[Block] = []
    blocks.append(Block(
        block_type="text",
        value=f"{release.project} released new version: {release.version}"
    ))
    blocks.append(Block(
        block_type="text",
        value=f"release date: {release_time}"
    ))
    message = Message(blocks=blocks)

    client = ChannelOpenApiClient()
    client.send_teamchat_message(message)

    return {"success": True}

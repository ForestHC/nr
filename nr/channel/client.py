from ..configs.config import settings
from .message import Message
from dataclasses import asdict
from requests import Response

import requests

from ..utils.dict_util import to_nullified_json


class ChannelOpenApiClient:
    def __init__(self) -> None:
        self._headers = {
            "x-access-key": settings.channel_open_api_access_key,
            "x-access-secret": settings.channel_open_api_access_secret
        }
        self._url = settings.channel_open_api_base_url
        self._version = settings.channel_open_api_version
        self._group_id = settings.channel_group_id

    def send_group_message(self, message: Message) -> None:
        url = f"{self._url}" \
            + f"/open/{self._version}" \
            + f"/groups/{self._group_id}" \
            + "/messages?botName=NewReleases.io"

        response: Response = requests.post(
            url=url,
            headers=self._headers,
            json=to_nullified_json(asdict(message))
        )

        print(response.json())

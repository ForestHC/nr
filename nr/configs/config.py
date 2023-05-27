from pydantic import BaseSettings
from pydantic.types import StrictStr


class Settings(BaseSettings):
    channel_open_api_base_url: StrictStr = "https://api.channel.io"
    channel_open_api_version: StrictStr = "v5"
    channel_open_api_access_key: StrictStr = ""
    channel_open_api_access_secret: StrictStr = ""
    channel_group_id: StrictStr = "96844"
    newreleases_webhook_verify_key: StrictStr = ""


settings = Settings()

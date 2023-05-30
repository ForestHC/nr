from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class Note(BaseModel):
    title: Optional[str]
    message: Optional[str]


class Account(BaseModel):
    _type: Field(str, alias="type")
    _id: Field(str, alias="id")
    name: str

class Tag(BaseModel):
    _id: Field(str, alias="id")
    name: str


class ReleaseHook(BaseModel):
    provider: str
    project: str
    version: str
    time: datetime
    cve: Optional[List[str]]
    is_prerelease: Optional[bool]
    is_updated: Optional[bool]
    note: Optional[Note]
    account: Account
    tags: Optional[Tag]
    project_note: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "provider": "github",
                "project": "nodejs/node",
                "version": "v11.5.0",
                "time": "2018-12-30T16:08:51.864468Z",
                "is_prerelease": True,
                "is_updated": True,
                "note": {
                    "title": "Release v11.5.0",
                    "message": "Release features\u003cbr\u003eBugfixes"
                },
                "account": {
                    "type": "user",
                    "id": "fwykdar796rkd6s2hwmqvhpsd1",
                    "name": "My Account Name"
                }
            }
        }

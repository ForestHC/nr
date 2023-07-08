from dataclasses import dataclass

from typing import List


@dataclass
class Block:
    type: str
    value: str


@dataclass
class Message:
    blocks: List[Block]
    options: List[str] | None

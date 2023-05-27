from typing import List

class Block:
    def __init__(self, block_type: str, value: str):
        self._block_type = block_type
        self._value = value

    def to_dict(self):
        return {
            "type": self._block_type,
            "value": self._value
        }

class Message:
    def __init__(self, blocks: List[Block], options: List[str] | None = None):
        self.blocks = blocks
        self.options = options

    def to_dict(self):
        return {
            "blocks": [block.to_dict() for block in self.blocks],
            "options": self.options
        }

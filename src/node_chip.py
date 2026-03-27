from enum import Enum

class ChipType(Enum):
    WHITE = "white"
    BLACK = "black"
    NONE = "none"

class ChipNode:
    def __init__(self, type, neighbors = {
        left: ChipType.NONE,
        right: ChipType.NONE,
        top: ChipType.NONE,
        bottom: ChipType.NONE
    })
        self.type = type
        self.neighbors = neighbors
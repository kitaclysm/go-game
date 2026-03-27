from enum import Enum

class ChipType(Enum):
    WHITE = "white"
    BLACK = "black"
    NONE = "none"

class ChipNode:
    def __init__(self, chip_type, coordx, coordy, neighbors = {
        left: ChipType.NONE,
        right: ChipType.NONE,
        top: ChipType.NONE,
        bottom: ChipType.NONE
    })
        self.chip_type = chip_type
        self.coordx = coordx
        self.coordy = coordy
        self.neighbors = neighbors
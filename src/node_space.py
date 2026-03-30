from enum import Enum

class SpaceType(Enum):
    WHITE = "white"
    BLACK = "black"
    EMPTY = "empty"

class SpaceNode:
    def __init__(self, row, col)
        self.state = SpaceType.EMPTY
        self.row = row
        self.col = col
        self.neighbors = []

    def __repr__(self):
        return f"SpaceNode({self.state}, {self.row}, {self.col}, {self.neighbors})"
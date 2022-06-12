from enum import Enum
from typing import Tuple

CellPosition = Tuple[int, int]


class CellType(Enum):
    FREE = 0
    OBSTACLE = 1
    START = 2
    GOAL = 3


class Cell:
    def __init__(self, y: int, x: int, cell_type: CellType = None):
        """
        Inicializa uma célula que representa um bloco do labirinto.
        :param y: posição vertical da célula.
        :param x: posição horizontal da célula.
        :param cell_type: tipo da célula.
        """
        self.y = y
        self.x = x
        self.type = cell_type if cell_type else CellType.FREE
        self.position: CellPosition = (x, y)

    def __eq__(self, other: 'Cell') -> bool:
        return self.position == other.position

    def __lt__(self, other: 'Cell') -> bool:
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other: 'Cell') -> bool:
        return (self.x > other.x) and (self.y > other.y)

    def __hash__(self) -> int:
        return hash(self.position)

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y})'

    def __sub__(self, other: 'Cell') -> float:
        return 1 if (abs(self.x - other.x) + abs(self.y - other.y)) == 1 else 1.4142135623730951

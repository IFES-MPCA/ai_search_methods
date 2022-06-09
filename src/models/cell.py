from enum import Enum
from typing import Tuple

CellPosition = Tuple[int, int]


class CellType(Enum):
    FREE = 0
    OBSTACLE = 1
    START = 2
    GOAL = 3


class Cell:
    def __init__(self, y: int, x: int, previous: 'Cell' = None,
                 cell_type: CellType = None):
        """
        Inicializa uma célula que representa um bloco do labirinto.
        :param y: posição vertical da célula.
        :param x: posição horizontal da célula.
        :param previous: célula precedente à célula atual.
        """
        self.y = y
        self.x = x
        self.type = cell_type if cell_type else CellType.FREE
        self.position: CellPosition = (x, y)

    def __repr__(self) -> str:
        return str(self.position)

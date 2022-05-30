from enum import Enum
from typing import List, Tuple, Dict


class CellType(Enum):
    FREE = 0
    OBSTACLE = 1
    START = 2
    GOAL = 3


value_to_enum: Dict[int, CellType] = {
    0: CellType.FREE,
    1: CellType.OBSTACLE,
    2: CellType.START,
    3: CellType.GOAL
}


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
        self.type = value_to_enum[
            cell_type] if cell_type in value_to_enum else CellType.FREE

        # todo: apagar associação desnecessário
        self.previous = previous
        self.position: Tuple[int, int] = (x, y)

    # todo: apagar método desnecessário
    def reconstruct_path(self) -> List['Cell']:
        current_cell = self
        path = [current_cell]

        while current_cell.previous:
            current_cell = current_cell.previous
            path.insert(0, current_cell)
        return path

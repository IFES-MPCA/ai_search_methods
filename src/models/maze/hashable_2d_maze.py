from typing import List, Optional, Tuple, Dict

from src.models.cell import CellType, Cell, CellPosition


class Hashable2DMaze:

    def __init__(self, n_lines: int, n_columns: int, seed=None, obstacles_chance: float = 0.25):
        self.lines = n_lines
        self.columns = n_columns
        self.maze: Dict[Tuple[int, int], Cell] = {}
        self.__generate__(n_lines, n_columns)
        self.__insert_obstacles__(n_lines, n_columns, obstacles_chance, seed)

    def __contains__(self, item: CellPosition) -> bool:
        return item in self.maze

    def __generate__(self, n_lines: int, n_columns: int):
        for y in range(n_lines):
            for x in range(n_columns):
                self.maze[(x, y)] = Cell(y, x)

    def __insert_obstacles__(self, n_lines: int, n_columns: int, chance: float = 0.25, seed=None):
        import random
        random.seed(seed)
        obstacles_count = chance * n_lines * n_columns

        for _ in range(int(obstacles_count)):
            x = random.randint(0, n_columns - 1)
            y = random.randint(0, n_lines - 1)
            self.__insert_obstacle__(x, y)

    def __insert_obstacle__(self, x: int, y: int):
        self.maze[(x, y)].type = CellType.OBSTACLE

    def set_cell(self, cell: Cell):
        self.maze[(cell.x, cell.y)] = cell

    def get_cell(self, position: CellPosition) -> Optional[Cell]:
        return self.maze[position]

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        all_positions: List[CellPosition] = [
            (cell.x, cell.y - 1),
            (cell.x - 1, cell.y - 1),
            (cell.x + 1, cell.y - 1),
            (cell.x - 1, cell.y + 1),
            (cell.x, cell.y + 1),
            (cell.x + 1, cell.y + 1),
            (cell.x - 1, cell.y),
            (cell.x + 1, cell.y),
        ]

        return [
            Cell(pos[1], pos[0], cell, self.get_cell(pos).type) for pos in all_positions if
            pos in self.maze and self.maze[pos].type != CellType.OBSTACLE
        ]

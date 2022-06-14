from typing import Optional, Tuple, Dict

from src.models.problem.maze_2d.cell import CellType, Cell, CellPosition


class Hashable2DMaze:

    def __init__(self, n_lines: int, n_columns: int, seed=None, obstacles_percent: float = 0.25):
        self.lines = n_lines
        self.columns = n_columns
        self.maze: Dict[Tuple[int, int], Cell] = {}
        self.__generate__(n_lines, n_columns)
        self.__insert_obstacles__(n_lines, n_columns, obstacles_percent, seed)

    def __contains__(self, item: CellPosition) -> bool:
        return item in self.maze

    def __generate__(self, n_lines: int, n_columns: int):
        for y in range(n_lines):
            for x in range(n_columns):
                self.maze[(x, y)] = Cell(x=x, y=y)

    def __insert_obstacles__(self, n_rows: int, n_columns: int, chance: float = 0.25, seed=None):
        import random
        random.seed(seed)
        obstacles_count = chance * n_rows * n_columns
        range_obstacles = range(int(obstacles_count))

        for _ in range_obstacles:
            x = random.randint(0, n_columns - 1)
            y = random.randint(0, n_rows - 1)
            self.maze[(x, y)].type = CellType.OBSTACLE

    def set_cell(self, cell: Cell):
        self.maze[(cell.x, cell.y)] = cell

    def get_cell(self, position: CellPosition) -> Optional[Cell]:
        return self.maze[position]

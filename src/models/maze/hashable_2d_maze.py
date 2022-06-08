from typing import Tuple, List, Dict

from src.models.cell import CellType, Cell


class Hashable2DMaze:
    def __init__(self, n_lines: int, n_columns: int, seed=None, obstacles_chance: float = 0.25):
        self.maze: Dict[Tuple[int, int], Cell] = {}
        self.__generate(n_lines, n_columns)
        self.__insert_obstacles(n_lines, n_columns, obstacles_chance, seed)

    def __init__(self, default_maze: List[List[CellType]]):
        self.maze = {}
        for y in range(len(default_maze)):
            for x in range(len(default_maze[y])):
                self.maze[(x, y)] = Cell(y, x, None, default_maze[y][x])

    def __generate(self, n_lines: int, n_columns: int):
        for y in range(n_lines):
            for x in range(n_columns):
                self.maze[(x, y)] = Cell(y, x)

    def __insert_obstacles(self, n_lines: int, n_columns: int, chance: float = 0.25, seed=None):
        import random
        random.seed(seed)
        obstacles_count = chance * n_lines * n_columns

        for _ in range(int(obstacles_count)):
            x = random.randint(0, n_columns - 1)
            y = random.randint(0, n_lines - 1)
            self.__insert_obstacle(x, y)

    def __insert_obstacle(self, x: int, y: int):
        self.maze[(x, y)].type = CellType.OBSTACLE

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        all_positions: List[Tuple[int, int]] = [
            (cell.x, cell.y - 1),
            (cell.x - 1, cell.y - 1),
            (cell.x + 1, cell.y - 1),
            (cell.x - 1, cell.y + 1),
            (cell.x, cell.y + 1),
            (cell.x + 1, cell.y + 1),
            (cell.x - 1, cell.y),
            (cell.x + 1, cell.y),
        ]

        accessible_neighbors: List[Cell] = [
            Cell(pos[1], pos[0], cell, self.maze[pos].type) for pos in all_positions if
            pos in self.maze and self.maze[pos].type != CellType.OBSTACLE
        ]

        # todo: apagar associação desnecessária
        for neighbor in accessible_neighbors:
            neighbor.previous = cell

        return accessible_neighbors

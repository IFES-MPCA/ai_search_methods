from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Iterable, Optional, Tuple

from src.models.cell import Cell, CellType
from src.models.maze import DefaultMazeWithViewer, Hashable2DMaze


class SearchResponse:
    def __init__(self, path: List[Cell], cost: int, steps_count: int):
        self.path = path
        self.cost = cost
        self.steps_count = steps_count


class SearchMethod(ABC):

    def __init__(self, default_maze: DefaultMazeWithViewer, start: Cell, goal: Cell):
        self.hash_maze: Hashable2DMaze = Hashable2DMaze(default_maze.labirinto)
        start.type = CellType.START
        goal.type = CellType.GOAL
        self.start = start
        self.goal = goal
        self.viewer = default_maze
        self.__set_cell(start)
        self.__set_cell(goal)

    def __set_cell(self, cell: Cell):
        self.hash_maze.maze[(cell.x, cell.y)] = cell

    @abstractmethod
    def search(self) -> Optional[SearchResponse]:
        pass

    def update_viewer(self, frontier: Iterable[Tuple[int, int]],
                      expanded: Iterable[Tuple[int, int]]):
        stack_cells = [self.hash_maze.maze[position] for position in frontier]
        visited_cells = [self.hash_maze.maze[position] for position in expanded]
        self.viewer.update(generated=stack_cells, expanded=visited_cells)


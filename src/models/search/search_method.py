from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Iterable, Optional, Callable

from src.models.cell import CellPosition
from src.models.maze.default_2d_maze import DefaultMazeWithViewer
from src.models.maze.hashable_2d_maze import Cell, CellType, Hashable2DMaze

CallbackSearch = Callable[[Iterable[CellPosition], Iterable[CellPosition]], None]
ExternalCallbackSearch = Callable[[Iterable[Cell], Iterable[Cell]], None]


class SearchResponse:
    def __init__(self, path: List[Cell], cost: int, steps_count: int):
        self.path = path
        self.cost = cost
        self.steps_count = steps_count


class SearchMethod(ABC):

    def __init__(self, default_maze: DefaultMazeWithViewer, start: Cell, goal: Cell):
        self.maze: Hashable2DMaze = Hashable2DMaze(default_maze.labirinto)
        start.type = CellType.START
        goal.type = CellType.GOAL
        self.start = start
        self.goal = goal
        self.viewer = default_maze
        self.maze.set_cell(start)
        self.maze.set_cell(goal)

    @abstractmethod
    def solve(self, step_callback: CallbackSearch) -> Optional[SearchResponse]:
        pass

    def search(self, step_callback: Optional[ExternalCallbackSearch] = None) -> Optional[SearchResponse]:
        """
        Executa o algoritmo de busca e a cada passo invoca o callback.
        :param step_callback: Callback que recebe a fronteira e os nós já visitados.
        :return: Resultado da busca com o caminho, custo e número de passos.
        """
        def wrapper_callback(frontier: Iterable[CellPosition], expanded: Iterable[CellPosition]):
            if step_callback is None:
                return None

            stack_cells = [self.maze.get_cell(position) for position in frontier]
            visited_cells = [self.maze.get_cell(position) for position in expanded]
            return step_callback(stack_cells, visited_cells)

        return self.solve(wrapper_callback)

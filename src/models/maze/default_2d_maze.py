from abc import ABC, abstractmethod
from typing import List, Iterable, Tuple

from numpy import ndarray

from src.models.cell import CellType, Cell


class DefaultMazeWithViewer(ABC):

    def __init__(self, labirinto: List[List[CellType]], start: Cell, goal: Cell, zoom=50,
                 step_time_miliseconds=-1):
        """
        Modelo de labirinto padrão entregue pelo professor.
        Interface usada para poder interagir com as classes dadas pelo professor sem ter que
        alterar o código dado como modelo.

        :param labirinto: Matriz de células do labirinto.
        :param start: célula inicial
        :param goal: célula objetivo
        :param zoom: Grau de ampliação para visualização
        :param step_time_miliseconds: Delay entre cada passo da busca.
        """
        self.labirinto = labirinto
        pass

    @abstractmethod
    def update(self, generated: Iterable[Cell], expanded: Iterable[Cell],
               path: Iterable[Cell]) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def _increase_image_size(self, img: ndarray, zoom: int = 10) -> ndarray:
        pass

    @abstractmethod
    def _draw_grid(self, maze_img: ndarray, zoom: int) -> None:
        pass

    @abstractmethod
    def _draw_cells(self, maze_img: ndarray, cells: Iterable[Cell],
                    color: Tuple[int, int, int]) -> None:
        pass

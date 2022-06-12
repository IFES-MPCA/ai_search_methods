from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Iterable, Optional, Callable, Generic

from src.models.base import T
from src.models.problem.search_problem import SearchProblem

CallbackSearch = Callable[[Iterable[T], Iterable[T]], None]
ExternalCallback = Callable[[Iterable[T], Iterable[T]], None]


class SearchResponse:
    def __init__(self, path: List[T], cost: int, steps_count: int):
        self.path = path
        self.cost = cost
        self.steps_count = steps_count


class SearchFunction(ABC, Generic[T]):

    def __init__(self, problem: SearchProblem[T], step_callback: Optional[ExternalCallback] = None):
        """
        Inst
        :param problem: Callback que recebe a fronteira e os nós já visitados.
        :param step_callback: Callback que recebe a fronteira e os nós já visitados.
        :return: Resultado da busca com o caminho, custo e número de passos.
        """
        self.problem = problem
        self.on_step = step_callback

    @abstractmethod
    def solve(self) -> Optional[SearchResponse]:
        pass

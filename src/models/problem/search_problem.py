from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterable

T = TypeVar('T')


class SearchProblem(ABC, Generic[T]):

    @abstractmethod
    def start_state(self) -> T:
        pass

    @abstractmethod
    def is_goal_state(self, state: T) -> bool:
        pass

    @abstractmethod
    def calculate_cost(self, current_state: T) -> int:
        pass

    @abstractmethod
    def get_successors(self, state: T) -> Iterable[T]:
        pass

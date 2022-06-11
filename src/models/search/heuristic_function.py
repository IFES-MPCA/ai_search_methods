from abc import abstractmethod, ABC
from typing import Generic

from src.models.base import T


class HeuristicFunction(ABC, Generic[T]):

    @abstractmethod
    def calculate(self, state: T, goal_state: T) -> float:
        pass

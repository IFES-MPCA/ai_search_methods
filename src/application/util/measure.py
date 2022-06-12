from time import time
from typing import Callable, TypeVar, Generic

from src.models.base import T

Params = TypeVar('Params')
Return = TypeVar('Return')


class TimeItResponse(Generic[T]):
    def __init__(self, value: T, time_in_ms: int):
        self.value = value
        self.time_in_ms = time_in_ms


def measure(function: Callable[[], Return]) -> TimeItResponse[Return]:
    """
    Define um decorador que mede o tempo de execução de uma função.
    :param function: função que terá seu tempo de execução medido.
    :return: função de entrada decorada com a medição de tempo.
    """

    start = int(round(time() * 1000))
    response = function()
    duration = int(round(time() * 1000)) - start

    return TimeItResponse(response, duration)

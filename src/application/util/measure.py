from functools import wraps
from time import time
from typing import Callable


def measure(function: Callable) -> Callable:
    """
    Define um decorador que mede o tempo de execução de uma função.
    :param function: função que terá seu tempo de execução medido.
    :return: função de entrada decorada com a medição de tempo.
    """
    @wraps(function)
    def __time_it__(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return function(*args, **kwargs)

        finally:
            end_ = int(round(time() * 1000)) - start
            class_name, fn_name = function.__qualname__.split('.')
            print(f"{class_name} -> {end_ if end_ > 0 else 0} ms")

    return __time_it__

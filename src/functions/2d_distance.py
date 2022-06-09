from typing import Tuple

"""Tupla representando o par de posições (x, y)"""
Point2D = Tuple[int, int]


def calculate_euclidian_distance(point_a: Point2D, point_b: Point2D) -> float:
    """
    Calcula a distância euclidiana entre dois pontos.
    :param point_a: Primeiro par ordenado (x, y)
    :param point_b: Segundo par ordenado (x, y)
    :return: Distância euclidiana entre os dois pontos recebidos
    """
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** 0.5

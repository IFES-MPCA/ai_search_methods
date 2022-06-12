from src.models.problem.maze_2d.cell import Cell
from src.models.search.heuristic_function import HeuristicFunction


class ManhattanCost(HeuristicFunction[Cell]):

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        """
        Calcula a distância de manhattan entre duas células/blocos.
        :param state: Célula atual
        :param goal_state: Célula objetivo
        :return: Distância de manhattan entre os dois pontos recebidos
        """
        return abs(goal_state.x - state.x) + abs(goal_state.y - state.y)


class EuclidianCost(HeuristicFunction[Cell]):

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        """
        Calcula a distância euclidiana entre duas células/blocos.
        :param state: Célula atual
        :param goal_state: Célula objetivo
        :return: Distância euclidiana entre os dois pontos recebidos
        """
        return ((state.x - goal_state.x) ** 2 + (state.y - goal_state.y) ** 2) ** 0.5

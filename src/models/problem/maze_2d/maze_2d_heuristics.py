from src.models.problem.maze_2d.cell import Cell
from src.models.search.heuristic_function import HeuristicFunction


class OctileCost(HeuristicFunction[Cell]):
    """
    Calcula a distância octil entre duas células

    Fonte da fórmula: https://www.sciencedirect.com/science/article/pii/S1000936116301182

    :param state: Célula atual
    :param goal_state: Célula objetivo
    :return: Distância euclidiana entre os dois pontos recebidos
    """
    D2 = 1.414

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        dx = abs(state.x - goal_state.x)
        dy = abs(state.y - goal_state.y)
        return self.D2 * min(dx, dy) + abs(dx - dy)


class EuclidianCost(HeuristicFunction[Cell]):

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        """
        Calcula a distância euclidiana entre duas células/blocos.
        :param state: Célula atual
        :param goal_state: Célula objetivo
        :return: Distância euclidiana entre os dois pontos recebidos
        """
        return ((state.x - goal_state.x) ** 2 + (state.y - goal_state.y) ** 2) ** 0.5

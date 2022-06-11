from src.functions.distance_2d import calc_euclidian_distance
from src.models.cell import Cell
from src.models.search.heuristic_function import HeuristicFunction


class ManhattanCost(HeuristicFunction[Cell]):

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        return abs(goal_state.x - state.x) + abs(goal_state.y - state.y)


class EuclidianCost(HeuristicFunction[Cell]):

    def calculate(self, state: Cell, goal_state: Cell) -> float:
        return calc_euclidian_distance(state.position, goal_state.position)

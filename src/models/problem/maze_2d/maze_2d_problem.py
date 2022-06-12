from typing import Iterable, List

from src.models.cell import Cell, CellType, CellPosition
from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.search_problem import SearchProblem


class Maze2DProblem(SearchProblem[Cell]):

    def __init__(self, maze: Hashable2DMaze, start: Cell, goal: Cell):
        self.maze: Hashable2DMaze = maze
        start.type = CellType.START
        goal.type = CellType.GOAL
        self.start = start
        self.goal = goal
        self.maze.set_cell(start)
        self.maze.set_cell(goal)

    def start_state(self) -> Cell:
        return self.start

    def goal_state(self) -> Cell:
        return self.goal

    def is_goal_state(self, state: Cell) -> bool:
        return state.position == self.goal.position

    def calculate_cost(self, actions: List[Cell]) -> int:
        index_range = range(len(actions) - 1)
        return sum((actions[i] - actions[i + 1]) for i in index_range)

    def __valid_position__(self, position: CellPosition) -> bool:
        if position[0] < 0 or position[0] >= self.maze.columns:
            return False

        if position[1] < 0 or position[1] >= self.maze.lines:
            return False

        return self.maze.get_cell(position).type != CellType.OBSTACLE

    def get_successors(self, state: Cell) -> Iterable[Cell]:
        all_positions: List[CellPosition] = sorted([
            (state.x, state.y - 1),
            (state.x - 1, state.y - 1),
            (state.x + 1, state.y - 1),
            (state.x - 1, state.y + 1),
            (state.x, state.y + 1),
            (state.x + 1, state.y + 1),
            (state.x - 1, state.y),
            (state.x + 1, state.y),
        ])
        return [
            Cell(position[1], position[0], state, self.maze.get_cell(position).type)
            for position in all_positions if self.__valid_position__(position)
        ]

from typing import Iterable, List

from src.models.cell import Cell, CellType, CellPosition
from src.models.maze.default_2d_maze import DefaultMazeWithViewer
from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.search_problem import SearchProblem


class Maze2DProblem(SearchProblem[Cell]):

    def __init__(self, default_maze: DefaultMazeWithViewer, start: Cell, goal: Cell):
        self.maze: Hashable2DMaze = Hashable2DMaze(default_maze.labirinto)
        start.type = CellType.START
        goal.type = CellType.GOAL
        self.start = start
        self.goal = goal
        self.viewer = default_maze
        self.maze.set_cell(start)
        self.maze.set_cell(goal)

    def start_state(self) -> Cell:
        return self.start

    def is_goal_state(self, state: Cell) -> bool:
        return state.type == CellType.GOAL or state.position == self.goal.position

    def calculate_cost(self, current_state: Cell) -> int:
        return 

    def get_successors(self, state: Cell) -> Iterable[Cell]:
        all_positions: List[CellPosition] = [
            (state.x, state.y - 1),
            (state.x - 1, state.y - 1),
            (state.x + 1, state.y - 1),
            (state.x - 1, state.y + 1),
            (state.x, state.y + 1),
            (state.x + 1, state.y + 1),
            (state.x - 1, state.y),
            (state.x + 1, state.y),
        ]
        return [
            Cell(position[1], position[0], state, self.maze.get_cell(position).type)
            for position in all_positions if position in self.maze and self.maze.get_cell(position).type != CellType.OBSTACLE
        ]

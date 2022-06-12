from typing import Iterable, Optional

from src.application.util.config import Config
from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.maze_2d.cell import Cell, CellType
from src.models.problem.maze_2d.maze_2d_heuristics import ManhattanCost
from src.models.problem.maze_2d.maze_2d_problem import Maze2DProblem
from src.models.problem.search_problem import SearchProblem
from src.models.search.methods.a_star import AStar
from src.models.search.search_function import SearchFunction, SearchResponse
from src.ui.maze_viewer import MazeViewer


def run(method: SearchFunction[Cell], times: int, viewer: MazeViewer, enable_visualization=False):
    def on_step_callback(generated: Iterable[Cell], expanded: Iterable[Cell]):
        viewer.update(generated=generated, expanded=expanded)

    for i in range(times):
        response: Optional[SearchResponse[Cell]] = None

        if enable_visualization:
            response = method.solve(on_step_callback)
            viewer.update(path=response.path)
            viewer.pause()

        else:
            response = method.solve()


def main():
    n_lines = 50
    n_columns = n_lines

    start = Cell(x=0, y=0, cell_type=CellType.START)
    goal = Cell(x=n_columns - 1, y=n_lines - 1, cell_type=CellType.GOAL)

    maze_2d = Hashable2DMaze(n_lines, n_columns, Config.seed, Config.obstacles_percentage)
    viewer = MazeViewer(start, goal, maze_2d, 5, 2)
    problem: SearchProblem[Cell] = Maze2DProblem(maze_2d, start, goal)

    heuristic = ManhattanCost()
    a_star: SearchFunction[Cell] = AStar(problem, heuristic)

    run(a_star, Config.n_executions, viewer, False)

    return 0


if __name__ == "__main__":
    main()

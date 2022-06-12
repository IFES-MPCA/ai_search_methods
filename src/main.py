from typing import Iterable

from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.maze_2d.cell import Cell
from src.models.problem.maze_2d.maze_2d_heuristics import ManhattanCost
from src.models.problem.maze_2d.maze_2d_problem import Maze2DProblem
from src.models.problem.search_problem import SearchProblem
from src.models.search.methods.a_star import AStar
from src.models.search.search_function import CallbackSearch, SearchFunction
from src.ui.maze_viewer import MazeViewer


def main():
    seed = 42  # coloque None no lugar do 42 para deixar aleatorio
    obstacles_percent = 0.25

    n_lines = 50
    n_columns = n_lines
    start = Cell(y=0, x=0)
    goal = Cell(y=n_lines - 1, x=n_columns - 1)

    maze_2d = Hashable2DMaze(n_lines, n_columns, seed, obstacles_percent)
    viewer = MazeViewer(start, goal, maze_2d, 5, 2)
    problem: SearchProblem[Cell] = Maze2DProblem(maze_2d, start, goal)

    def on_step_callback(generated: Iterable[Cell], expanded: Iterable[Cell]):
        viewer.update(generated=[g for g in generated], expanded=[e for e in expanded])

    on_step: CallbackSearch[Cell] = on_step_callback

    # bfs: SearchFunction[Cell] = BreadthFirstSearch(problem, on_step)
    # r = bfs.solve()

    # dfs: SearchFunction[Cell] = DepthFirstSearch(problem, on_step)
    # r = dfs.solve()

    # ucs: SearchFunction[Cell] = UniformCostSearch(problem, on_step)
    # r = ucs.solve()

    heuristic = ManhattanCost()
    a_star: SearchFunction[Cell] = AStar(problem, heuristic, on_step)
    r = a_star.solve()

    viewer.update(path=r.path)
    viewer.pause()
    return 0


if __name__ == "__main__":
    main()

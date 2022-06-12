import statistics
from typing import Iterable

from src.application.report.result_reporter import ReportResult
from src.application.util.config import Config
from src.application.util.measure import measure
from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.maze_2d.cell import Cell, CellType
from src.models.problem.maze_2d.maze_2d_heuristics import EuclidianCost
from src.models.problem.maze_2d.maze_2d_problem import Maze2DProblem
from src.models.problem.search_problem import SearchProblem
from src.models.search.methods.a_star import AStar
from src.models.search.methods.breadth_first_search import BreadthFirstSearch
from src.models.search.methods.depth_first_search import DepthFirstSearch
from src.models.search.methods.uniform_cost_search import UniformCostSearch
from src.models.search.search_function import SearchFunction, SearchResponse
from src.ui.maze_viewer import MazeViewer


def run(method: SearchFunction[Cell], viewer: MazeViewer, enable_visualization=False):
    def on_step_callback(generated: Iterable[Cell], expanded: Iterable[Cell]):
        viewer.update(generated, expanded)

    times = Config.n_executions
    seed = Config.seed

    results_reporter = ReportResult(times, viewer.lines, viewer.columns, seed)
    executions_time = []
    search_response: SearchResponse = None

    for i in range(times):
        if enable_visualization:
            search_response = method.solve(on_step_callback)
            viewer.update(path=search_response.path)
            viewer.pause()
            return

        else:
            response = measure(method.solve)
            search_response = response.value
            executions_time.append(response.time_in_ms)

    avg_time = sum(executions_time) / times
    std_time = statistics.pstdev(executions_time)
    cost = search_response.path_cost
    n_generated = search_response.generated
    n_expanded = search_response.expanded
    results_reporter.append_line(method.__class__.__name__, avg_time, std_time, cost, n_generated, n_expanded)


def main():
    for size in Config.maze_sizes:
        n_lines = size
        n_columns = size

        start = Cell(x=0, y=0, cell_type=CellType.START)
        goal = Cell(x=n_columns - 1, y=n_lines - 1, cell_type=CellType.GOAL)

        maze_2d = Hashable2DMaze(n_lines, n_columns, Config.seed, Config.obstacles_percentage)
        viewer = MazeViewer(start, goal, maze_2d, 5, 1)
        problem: SearchProblem[Cell] = Maze2DProblem(maze_2d, start, goal)

        heuristic = EuclidianCost()

        bfs: SearchFunction[Cell] = BreadthFirstSearch(problem)
        dfs: SearchFunction[Cell] = DepthFirstSearch(problem)
        ucs: SearchFunction[Cell] = UniformCostSearch(problem)
        a_star: SearchFunction[Cell] = AStar(problem, heuristic)
        all_methods = [a_star]

        for method in all_methods:
            run(method, viewer, enable_visualization=False)

    return 0


if __name__ == "__main__":
    print(measure(main).time_in_ms)

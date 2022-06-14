import statistics
from typing import Iterable

from src.application.report.result_reporter import ReportResult
from src.application.util.config import Config
from src.application.util.measure import measure
from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.maze_2d.cell import Cell, CellType
from src.models.problem.maze_2d.maze_2d_heuristics import EuclidianCost, OctileCost
from src.models.problem.maze_2d.maze_2d_problem import Maze2DProblem
from src.models.problem.search_problem import SearchProblem
from src.models.search.methods.a_star import AStar
from src.models.search.methods.breadth_first_search import BreadthFirstSearch
from src.models.search.methods.depth_first_search import DepthFirstSearch
from src.models.search.methods.uniform_cost_search import UniformCostSearch
from src.models.search.search_function import SearchFunction, SearchResponse
from src.ui.maze_viewer import MazeViewer


def run(method: SearchFunction[Cell], method_name: str, viewer: MazeViewer, enable_visualization=False):
    def on_step_callback(generated: Iterable[Cell], expanded: Iterable[Cell]):
        viewer.update(generated, expanded)

    times = Config.n_executions
    seed = Config.seed

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

        if not search_response:
            raise Exception("Não foi possível encontrar o caminho. Verifique se o labirinto é solúvel.")

    if not enable_visualization:
        results_reporter = ReportResult(times, viewer.lines, viewer.columns, seed)
        avg_time = sum(executions_time) / times
        std_time = statistics.pstdev(executions_time)
        path = search_response.path
        cost = search_response.path_cost
        n_generated = search_response.generated
        n_expanded = search_response.expanded
        results_reporter.append_line(method_name, avg_time, std_time, cost, len(path), n_generated, n_expanded)


def print_config(size: int):
    print('Executando com:')
    print(f'- Número de execuções: {Config.n_executions}')
    print(f'- Dimensão labirinto: {size}x{size}')
    print(f'- Seed: {Config.seed}')
    print(f'- Porcentagem de obstáculos: {Config.obstacles_percentage * 100}%')
    print('-----')


def main():
    for size in Config.maze_sizes:
        print_config(size)
        n_lines = size
        n_columns = size

        start = Cell(x=0, y=0, cell_type=CellType.START)
        goal = Cell(x=n_columns - 1, y=n_lines - 1, cell_type=CellType.GOAL)

        maze_2d = Hashable2DMaze(n_lines, n_columns, Config.seed, Config.obstacles_percentage)
        viewer = MazeViewer(start, goal, maze_2d, 5, 1)
        problem: SearchProblem[Cell] = Maze2DProblem(maze_2d, start, goal)

        euclidian_heuristic = EuclidianCost()
        manhattan_heuristic = OctileCost()

        bfs: SearchFunction[Cell] = BreadthFirstSearch(problem)
        dfs: SearchFunction[Cell] = DepthFirstSearch(problem)
        ucs: SearchFunction[Cell] = UniformCostSearch(problem)
        a_star_euclidian: SearchFunction[Cell] = AStar(problem, euclidian_heuristic)
        a_star_octil: SearchFunction[Cell] = AStar(problem, manhattan_heuristic)
        all_methods = [
            (bfs, 'Breath First Search'),
            (ucs, 'Uniform Cost Search'),
            (a_star_octil, 'A* (Octile)'),
            (a_star_euclidian, 'A* (Euclidian)'),
            (dfs, 'Depth First Search')
        ]

        # Passe True para habilitar a visualização de cada algoritmo
        for method, name in all_methods:
            run(method, name, viewer, enable_visualization=False)

    print('Fim da execução')
    return 0


if __name__ == "__main__":
    main()

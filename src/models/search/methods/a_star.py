from queue import PriorityQueue
from typing import Optional, List, Tuple, Set

from src.application.util.measure import measure
from src.models.base import T
from src.models.problem.search_problem import SearchProblem
from src.models.search.heuristic_function import HeuristicFunction
from src.models.search.search_function import SearchFunction, SearchResponse

PriorityQueueItem = Tuple[float, Tuple[T, List[T]]]


class AStar(SearchFunction):

    def __init__(self, problem: SearchProblem[T], heuristic: HeuristicFunction):
        super().__init__(problem)
        self.heuristic = heuristic

    @measure
    def solve(self, step_callback=None) -> Optional[SearchResponse]:
        frontier: PriorityQueue[PriorityQueueItem] = PriorityQueue()
        frontier_set: Set[T] = set()
        visited: Set[T] = set()
        actions: List[T] = []

        current_state = self.problem.start_state()
        frontier.put((0, (current_state, actions)))
        frontier_set.add(current_state)

        while not frontier.empty():
            priority, path = frontier.get()
            frontier_set.remove(path[0])
            current_state = path[0]
            actions = path[1]

            if self.problem.is_goal_state(current_state):
                return SearchResponse(actions, len(actions), len(visited))

            if current_state in visited or current_state in frontier_set:
                continue

            visited.add(current_state)
            neighbors = self.problem.get_successors(current_state)

            for child_state in neighbors:
                if child_state in visited or child_state in frontier_set:
                    continue

                moves = actions + [child_state]

                g_cost = self.problem.calculate_cost(moves)
                h_cost = self.heuristic.calculate(child_state, self.problem.goal_state())
                cost = g_cost + h_cost
                frontier.put((cost, (child_state, moves)))
                frontier_set.add(child_state)

            if step_callback:
                frontier_cells = [item[0] for cost, item in frontier.queue]
                step_callback(frontier_cells, visited)

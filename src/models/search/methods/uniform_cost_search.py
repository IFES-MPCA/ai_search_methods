from queue import PriorityQueue
from typing import Optional, List, Tuple, Set

from src.application.util.measure import measure
from src.models.base import T
from src.models.search.search_function import SearchFunction, SearchResponse

PriorityQueueItem = Tuple[float, Tuple[T, List[T]]]


class UniformCostSearch(SearchFunction):

    @measure
    def solve(self) -> Optional[SearchResponse]:
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
                cost = self.problem.calculate_cost(moves)
                frontier.put((cost, (child_state, moves)))
                frontier_set.add(child_state)

            if self.on_step:
                frontier_cells = [item[0] for cost, item in frontier.queue]
                self.on_step(frontier_cells, visited)

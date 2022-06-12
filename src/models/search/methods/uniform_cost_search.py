from queue import PriorityQueue
from typing import Optional, List, Tuple, Set

from src.models.base import T
from src.models.search.search_function import SearchFunction, SearchResponse

PriorityQueueItem = Tuple[float, Tuple[T, List[T]]]


class UniformCostSearch(SearchFunction):

    def solve(self, step_callback=None) -> Optional[SearchResponse]:
        current_state = self.problem.start_state()

        frontier_set: Set[T] = {current_state}
        visited: Set[T] = set()
        actions: List[T] = [current_state]
        frontier: PriorityQueue[PriorityQueueItem] = PriorityQueue()
        frontier.put((0, (current_state, actions)))

        while not frontier.empty():
            priority, path = frontier.get()
            frontier_set.remove(path[0])
            current_state = path[0]
            actions = path[1]

            if self.problem.is_goal_state(current_state):
                return SearchResponse(actions, len(actions), len(frontier_set) + len(visited), len(visited))

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

            if step_callback:
                frontier_cells = [item[0] for cost, item in frontier.queue]
                step_callback(frontier_cells, visited)

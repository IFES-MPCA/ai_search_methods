import queue
from queue import Queue
from typing import List, Set, Optional, Tuple

from src.models.base import T
from src.models.search.search_function import SearchFunction, SearchResponse

State = Tuple[T, List[T]]


class BreadthFirstSearch(SearchFunction):

    def solve(self, step_callback=None) -> Optional[SearchResponse]:
        current_state: T = self.problem.start_state()

        frontier_set: Set[T] = {current_state}
        visited: Set[T] = set()
        actions: List[T] = [current_state]
        frontier: Queue[State] = queue.Queue()
        frontier.put((current_state, actions))

        while not frontier.empty():
            current_state, actions = frontier.get()
            frontier_set.remove(current_state)

            if current_state in visited or current_state in frontier_set:
                continue

            if self.problem.is_goal_state(current_state):
                return SearchResponse(actions, self.problem.calculate_cost(actions), len(frontier_set), len(visited))

            visited.add(current_state)
            neighbors = self.problem.get_successors(current_state)

            for child_state in neighbors:
                if child_state in visited or child_state in frontier_set:
                    continue

                frontier.put((child_state, actions + [child_state]))
                frontier_set.add(child_state)

            if step_callback:
                frontier_cells = [item for item, path in frontier.queue]
                step_callback(frontier_cells, visited)

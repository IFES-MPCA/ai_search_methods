from typing import List, Set, Optional, Tuple

from src.models.base import T
from src.models.search.search_function import SearchFunction, SearchResponse

State = Tuple[T, List[T]]


class DepthFirstSearch(SearchFunction):

    def solve(self) -> Optional[SearchResponse]:
        frontier: List[State] = []
        visited: Set[T] = set()
        actions: List[T] = []

        current_state: T = self.problem.start_state()
        frontier.append((current_state, actions))

        while frontier:
            current_state, actions = frontier.pop()

            if self.problem.is_goal_state(current_state):
                return SearchResponse(actions, len(actions), len(visited))

            if current_state in visited:
                continue

            visited.add(current_state)
            neighbors = sorted(self.problem.get_successors(current_state))

            for child_state in neighbors:
                if child_state in visited:
                    continue

                path = actions[:]
                path.append(child_state)
                frontier.append((child_state, path))

            if self.on_step:
                frontier_cells = [item for item, path in frontier]
                self.on_step(frontier_cells, visited)

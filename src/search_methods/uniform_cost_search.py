from queue import PriorityQueue
from typing import Optional, List, Tuple

from src.functions.distance_2d import calc_euclidian_distance
from src.models.cell import Cell, CellType, CellPosition
from src.search_methods.search_method import SearchMethod, CallbackSearch, SearchResponse

PriorityQueueItem = Tuple[float, Tuple[CellPosition, Optional[CellPosition], List[CellPosition]]]


class UniformCostSearch(SearchMethod):

    def calc_cost(self, states: List[CellPosition]) -> float:
        return sum([calc_euclidian_distance(states[i], states[i + 1]) for i in range(len(states) - 2)])

    def solve(self, step_callback: CallbackSearch) -> Optional[SearchResponse]:
        frontier: PriorityQueue[PriorityQueueItem] = PriorityQueue()
        current_cell: Cell = self.start
        visited: List[CellPosition] = []
        actions: List[CellPosition] = []

        frontier.put((0, (current_cell.position, None, actions)))

        while not frontier.empty():
            priority, current_path = frontier.get()
            current_state = current_path[0]
            current_action = current_path[1]
            actions = current_path[2]
            current_cell = self.maze.get_cell(current_state)

            if current_cell.type is CellType.GOAL:
                step_callback(visited, actions)
                cells_path = [self.maze.get_cell(position) for position in actions]
                return SearchResponse(cells_path, len(cells_path), len(visited))

            if current_state not in visited:
                visited.append(current_state)
                neighbors = self.maze.get_neighbors(current_cell)

                for child_state in neighbors:
                    if child_state.position in visited:
                        continue
                    moves = actions.copy()
                    moves.append(child_state.position)

                    cost = self.calc_cost(moves)
                    frontier.put((cost, (child_state.position, child_state.position, moves)))

            temp = [item[0] for cost, item in frontier.queue]
            step_callback(temp, visited)

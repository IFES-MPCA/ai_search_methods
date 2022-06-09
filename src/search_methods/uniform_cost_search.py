from queue import PriorityQueue
from typing import Optional, Set, List, Tuple

from src.models.cell import Cell, CellType, CellPosition
from src.search_methods.search_method import SearchMethod, CallbackSearch, SearchResponse


class UniformCostSearch(SearchMethod):

    def solve(self, step_callback: CallbackSearch) -> Optional[SearchResponse]:
        frontier: PriorityQueue[Tuple[int, CellPosition]] = PriorityQueue()
        frontier_set: Set[CellPosition] = set()

        expanded_set: Set[CellPosition] = set()
        expanded_in_order: List[Cell] = []

        current_cell: Cell = self.start
        current_position: CellPosition = self.start.position
        frontier.put((0, current_position))
        frontier_set.add(current_position)

        while not frontier.empty():
            current_cost, current_position = frontier.get()

            if current_position in frontier_set:
                frontier_set.remove(current_position)

            if current_position in expanded_set:
                continue

            current_cell = self.maze.get_cell(current_position)
            expanded_set.add(current_position)
            expanded_in_order.append(current_cell)

            if current_cell.type is CellType.GOAL:
                break

            neighbors = self.maze.get_neighbors(current_cell)

            for adjacent_cell in neighbors:
                if adjacent_cell.position not in expanded_set or adjacent_cell.position not in frontier_set:
                    frontier.put((current_cost + 1, adjacent_cell.position))
                    frontier_set.add(adjacent_cell.position)

            step_callback([v for p, v in frontier.queue], expanded_set)

        if current_cell.type is not CellType.GOAL:
            return None

        step_callback([v for p, v in frontier.queue], expanded_set)
        visited_cells = [self.maze.get_cell(position.position) for position in expanded_in_order]
        return SearchResponse(visited_cells, len(expanded_set), len(expanded_set))

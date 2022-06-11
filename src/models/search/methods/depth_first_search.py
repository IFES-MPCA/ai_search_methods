from typing import List, Set, Optional, Tuple

from src.models.cell import CellPosition
from src.models.maze.hashable_2d_maze import CellType, Cell
from src.search_methods.search_method import SearchMethod, SearchResponse, CallbackSearch


class DepthFirstSearch(SearchMethod):

    def solve(self, step_callback: CallbackSearch) -> Optional[SearchResponse]:
        current_cell: Cell = self.start

        # Armazenar somente a tupla (x, y), pois ela é imutável e podemos usar o operator IN
        # nativo das estruturas de dados

        # Lista de nós a serem visitados (fronteira)
        stack: List[CellPosition] = [self.start.position]

        # Lista de nós já visitados, uso de conjunto com tuplas para evitar
        # repetição e acelerar comparação usando o operador IN
        expanded_set: Set[CellPosition] = set()
        expanded_in_order: List[CellPosition] = []

        while stack:
            current_position = stack.pop()

            if current_position in expanded_set:
                continue

            current_cell = self.maze.get_cell(current_position)
            expanded_set.add(current_position)
            expanded_in_order.append(current_position)

            if current_cell.type is CellType.GOAL:
                break

            neighbors = self.maze.get_neighbors(current_cell)

            for adjacent_cell in neighbors:
                if adjacent_cell.position in expanded_set or adjacent_cell.position in stack:
                    continue

                stack.append(adjacent_cell.position)

            step_callback(stack, expanded_set)

        if current_cell.type is not CellType.GOAL:
            return None

        step_callback(stack, expanded_set)
        visited_cells = [self.maze.get_cell(position) for position in expanded_in_order]
        return SearchResponse(visited_cells, len(expanded_set), len(expanded_set))

from typing import List, Set, Optional, Tuple

from src.models.maze.hashable_2d_maze import CellType, Cell
from src.search_methods.search_method import SearchMethod, SearchResponse


class DepthFirstSearch(SearchMethod):

    def search(self) -> Optional[SearchResponse]:
        current_cell: Cell = self.start

        # Armazenar somente a tupla (x, y), pois ela é imutável e podemos usar o operator IN
        # nativo das estruturas de dados

        # Lista de nós a serem visitados
        stack: List[Tuple[int, int]] = [self.start.position]

        # Lista de nós já visitados
        visited: Set[Tuple[int, int]] = set()

        while stack:
            current_position = stack.pop()

            if current_position in visited:
                continue

            visited.add(current_position)
            current_cell = self.hash_maze.maze[current_position]

            if current_cell.type is CellType.GOAL:
                break

            neighbors = self.hash_maze.get_neighbors(current_cell)

            for adjacent_cell in neighbors:
                if adjacent_cell.position in visited or adjacent_cell.position in stack:
                    continue
                stack.append(adjacent_cell.position)

                if adjacent_cell.type == CellType.GOAL or adjacent_cell.type == CellType.GOAL.value:
                    print(f'Goal found! {adjacent_cell.position}')
                    break

            self.update_viewer(stack, visited)

        if current_cell.type != CellType.GOAL:
            return None

        solution_path = current_cell.reconstruct_path()
        visited_cells = [self.hash_maze.maze[position] for position in visited]
        return SearchResponse(visited_cells, len(solution_path), len(visited))

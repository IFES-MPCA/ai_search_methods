from queue import PriorityQueue
from typing import Optional, Tuple, Set, Dict

from src.models.base import T
from src.models.search.methods.a_star import reconstruct_path
from src.models.search.search_function import SearchFunction, SearchResponse

PriorityQueueItem = Tuple[float, T]


class UniformCostSearch(SearchFunction):

    def solve(self, step_callback=None) -> Optional[SearchResponse]:
        current_state = self.problem.get_start_state()

        # nós que já foram explorados
        closed_states: Set[T] = set()

        # dicionários para evitar redundância de cálculo de heurística
        g_cost_by_state: Dict[T, float] = {current_state: 0}

        # dicionário para auxiliar na construção do caminho a partir do nó final
        predecessor_by_state: Dict[T, T] = {}

        # uso de set para evitar pesquisa na fila O(N)
        states_to_open_set: Set[T] = {current_state}

        # fila de prioridade ordenada pelo custo G
        states_to_open: PriorityQueue[PriorityQueueItem] = PriorityQueue()
        states_to_open.put((0, current_state))

        while states_to_open_set:
            priority, current_state = states_to_open.get()

            if self.problem.is_goal_state(current_state):
                final_path = reconstruct_path(predecessor_by_state, current_state)
                return SearchResponse(
                    final_path, self.problem.calculate_cost(final_path),
                    len(states_to_open_set), len(closed_states)
                )

            states_to_open_set.remove(current_state)
            neighbors = self.problem.get_successors(current_state)

            for neighbor in neighbors:
                new_g_score = g_cost_by_state[current_state] + self.problem.calculate_cost([current_state, neighbor])

                if neighbor not in g_cost_by_state or new_g_score < g_cost_by_state[neighbor]:
                    predecessor_by_state[neighbor] = current_state
                    g_cost_by_state[neighbor] = new_g_score

                    if neighbor not in states_to_open_set:
                        states_to_open.put((g_cost_by_state[neighbor], neighbor))
                        states_to_open_set.add(neighbor)

            closed_states.add(current_state)

            if step_callback:
                frontier_cells = [item for cost, item in states_to_open.queue]
                step_callback(frontier_cells, closed_states)

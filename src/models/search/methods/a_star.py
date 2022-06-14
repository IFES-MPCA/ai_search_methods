from queue import PriorityQueue
from typing import Optional, List, Tuple, Set, Dict

from src.models.base import T
from src.models.problem.search_problem import SearchProblem
from src.models.search.heuristic_function import HeuristicFunction
from src.models.search.search_function import SearchFunction, SearchResponse

PriorityQueueItem = Tuple[float, T]


def reconstruct_path(predecessor_by_state: Dict[T, T], current_state: T) -> List[T]:
    final_path = [current_state]

    while current_state in predecessor_by_state:
        current_state = predecessor_by_state[current_state]
        final_path.append(current_state)
    return final_path[::-1]


class AStar(SearchFunction):

    def __init__(self, problem: SearchProblem[T], heuristic: HeuristicFunction):
        super().__init__(problem)
        self.heuristic = heuristic

    def solve(self, step_callback=None) -> Optional[SearchResponse]:
        current_state = self.problem.start_state()
        goal_state = self.problem.goal_state()

        # nós que já foram explorados
        closed_states: Set[T] = set()

        # dicionários para evitar redundância de cálculo de heurística
        g_cost_by_state: Dict[T, float] = {current_state: 0}
        f_cost_by_state: Dict[T, float] = {current_state: self.heuristic.calculate(current_state, goal_state)}

        # dicionário para auxiliar na construção do caminho a partir do nó final
        predecessor_by_state: Dict[T, T] = {}

        # uso de set para evitar pesquisa na fila
        states_to_open_set: Set[T] = {current_state}

        states_to_open: PriorityQueue[PriorityQueueItem] = PriorityQueue()
        states_to_open.put((f_cost_by_state[current_state], current_state))

        while states_to_open_set:
            priority, current_state = states_to_open.get()

            if self.problem.is_goal_state(current_state):
                final_path = reconstruct_path(predecessor_by_state, current_state)
                return SearchResponse(
                    final_path, self.problem.calculate_cost(final_path),
                    len(states_to_open.queue), len(closed_states)
                )

            states_to_open_set.remove(current_state)

            neighbors = self.problem.get_successors(current_state)

            for neighbor in neighbors:

                if neighbor not in g_cost_by_state:
                    g_cost_by_state[neighbor] = float('inf')
                    f_cost_by_state[neighbor] = float('inf')

                new_g_score = g_cost_by_state[current_state] + self.heuristic.calculate(current_state, neighbor)

                if new_g_score < g_cost_by_state[neighbor]:
                    predecessor_by_state[neighbor] = current_state
                    g_cost_by_state[neighbor] = new_g_score
                    f_cost_by_state[neighbor] = new_g_score + self.heuristic.calculate(neighbor, goal_state)

                    if neighbor not in states_to_open_set:
                        states_to_open.put((f_cost_by_state[neighbor], neighbor))
                        states_to_open_set.add(neighbor)

            closed_states.add(current_state)

            if step_callback:
                frontier_cells = [item for cost, item in states_to_open.queue]
                step_callback(frontier_cells, closed_states)

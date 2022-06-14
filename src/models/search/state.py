from plistlib import Dict
from typing import List

from src.models.base import T


def reconstruct_path(predecessor_by_state: Dict[T, T], current_state: T) -> List[T]:
    final_path = [current_state]

    while current_state in predecessor_by_state:
        current_state = predecessor_by_state[current_state]
        final_path.append(current_state)
    return final_path[::-1]

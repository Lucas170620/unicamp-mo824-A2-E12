from typing import List, TypeVar

E = TypeVar('E')


class Solution(List[E]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cost = float('inf')
    
    def __str__(self) -> str:
        return f"Solution: cost=[{self.cost}], size=[{len(self)}], elements={super().__str__()}"

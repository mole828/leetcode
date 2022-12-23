from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([-1 if '--' in s else 1 for s in operations])
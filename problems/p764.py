from functools import cache
import itertools
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        res = 0

        D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        mines = {(i, j) for i, j in mines}

        @cache
        def helper(x, y, d):
            x, y = x + D[d][0], y + D[d][1]
            if 0 <= x < n and 0 <= y < n and (x, y) not in mines:
                return 1 + helper(x, y, d)
            return 0

        nl = sorted(range(n), key=lambda x:abs(n//2-x))
        for i, j in itertools.product(nl, nl):
            if min(i + 1, j + 1, n - i, n - j) <= res:
                continue
            if (i, j) not in mines:
                res = max(res, min(helper(i, j, k) for k in range(4)) + 1)
        
        return res
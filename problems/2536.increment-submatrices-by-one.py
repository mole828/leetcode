#
# @lc app=leetcode id=2536 lang=python3
#
# [2536] Increment Submatrices by One
#

# @lc code=start
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        return [row[:n] for row in diff[:n]]
        
# @lc code=end


#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i + 1 == j :
                return 0
            m = values[i] * values[j]
            return min(
                dfs(i, k) + dfs(k, j) + m * values[k]
                for k in range(i+1,j)
            )
        return dfs(0, len(values) - 1)
        
# @lc code=end


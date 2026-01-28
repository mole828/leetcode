#
# @lc app=leetcode id=3651 lang=python3
#
# [3651] Minimum Cost Path with Teleportations
#

# @lc code=start
# 手写 min 更快
from math import inf
from typing import List


min = lambda a, b: b if b < a else a

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        mx = max(map(max, grid))

        suf_min_f = [inf] * (mx + 2)
        for _ in range(k + 1):
            min_f = [inf] * (mx + 1)

            f = [inf] * (n + 1)
            f[1] = -grid[0][0] 
            for row in grid:
                for j, x in enumerate(row):
                    f[j + 1] = min(min(f[j], f[j + 1]) + x, suf_min_f[x])
                    min_f[x] = min(min_f[x], f[j + 1])

            for i in range(mx, -1, -1):
                suf_min_f[i] = min(suf_min_f[i + 1], min_f[i])

        return f[n]
# @lc code=end


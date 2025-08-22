#
# @lc app=leetcode id=3195 lang=python3
#
# [3195] Find the Minimum Area to Cover All Ones I
#

# @lc code=start
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_x = min(min_x, i)
                    min_y = min(min_y, j)
                    max_x = max(max_x, i)
                    max_y = max(max_y, j)
        return (max_x - min_x + 1) * (max_y - min_y + 1)

        
# @lc code=end


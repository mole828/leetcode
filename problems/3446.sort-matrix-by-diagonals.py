#
# @lc app=leetcode id=3446 lang=python3
#
# [3446] Sort Matrix by Diagonals
#

# @lc code=start
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        lines_value = { i: [] for i in range(-n+1, n) }
        lines_index = { i: [] for i in range(-n+1, n) }
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                lines_value[y-x].append((value))
                lines_index[y-x].append((y, x))
        for i in lines_value.keys():
            lines_value[i].sort(reverse=i>=0)
        for i in lines_value.keys():
            for value, (y, x) in zip(lines_value[i], lines_index[i]):
                grid[y][x] = value
        return grid
        
# @lc code=end

print(Solution().sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))
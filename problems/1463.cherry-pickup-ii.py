#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        @cache
        def dp(row: int, a: int, b: int) -> int:
            if row==rowLength:
                return 0 
            this = grid[row][a] if a==b else grid[row][a]+grid[row][b]
            return max(
                dp(row+1, nextA, nextB)
                for nextA in range(max(0,a-1),min(colLength,a+2))
                for nextB in range(max(0,b-1),min(colLength,b+2))
            ) + this 
        return dp(0, 0, colLength-1) 

# @lc code=end

print(Solution().cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
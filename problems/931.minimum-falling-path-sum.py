#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        lengthRow = len(matrix)
        lengthCol = len(matrix[0])
        @cache
        def dp(row: int, col: int) -> int:
            if row == lengthRow:
                return 0
            dp_result = min(
                dp(row+1, nextCol) for nextCol in range(
                    max(0, col-1), 
                    min(col+2, lengthCol)
                )
            ) + matrix[row][col]
            print(f"dp({row},{col}): {dp_result}")
            return dp_result
        return min(dp(0, col) for col in range(lengthCol))
        
        
# @lc code=end

print(Solution().minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
print(Solution().minFallingPathSum(matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
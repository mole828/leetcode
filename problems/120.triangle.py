#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
        
# @lc code=end


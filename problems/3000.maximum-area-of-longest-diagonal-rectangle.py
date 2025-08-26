#
# @lc app=leetcode id=3000 lang=python3
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#

# @lc code=start
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_power = 0
        max_area = 0
        for a,b in dimensions:
            diagonal_power = a*a + b*b
            if diagonal_power > max_diagonal_power:
                max_diagonal_power = diagonal_power
                max_area = a * b
            elif diagonal_power == max_diagonal_power:
                max_area = max(max_area, a * b)
        return max_area
# @lc code=end


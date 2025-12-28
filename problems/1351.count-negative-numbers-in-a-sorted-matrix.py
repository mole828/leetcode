#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(
            1
            for row in grid
            for num in row
            if num < 0
        )
# @lc code=end


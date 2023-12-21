#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        last = points[0][0]
        output = 0
        for x,y in points:
            dx = x - last 
            output = max(output, dx)
            last = x 
        return output
# @lc code=end


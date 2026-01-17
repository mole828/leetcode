#
# @lc app=leetcode id=3047 lang=python3
#
# [3047] Find the Largest Area of Square Inside Two Rectangles
#

# @lc code=start
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        for i, ((bx, by), (tx, ty)) in enumerate(zip(bottomLeft, topRight)):
            if tx - bx <= max_side or ty - by <= max_side:
                continue
            for j in range(i):
                bx2, by2 = bottomLeft[j]
                tx2, ty2 = topRight[j]
                width = min(tx, tx2) - max(bx, bx2)
                height = min(ty, ty2) - max(by, by2)
                side = min(width, height)
                max_side = max(max_side, side)
        return max_side ** 2

# @lc code=end


#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_places: List[tuple[int, int]] = []
        for y, row in enumerate(matrix):
            for x, num in enumerate(row):
                if num == 0:
                    zero_places.append((y, x))
        for (y, x) in zero_places:
            for i in range(rows):
                matrix[i][x] = 0
            for i in range(cols):
                matrix[y][i] = 0

# @lc code=end


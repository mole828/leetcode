#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(r: int, c: int) -> bool:
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in nums:
                        return False
                    nums.add(val)
            magic_sum = 15
            for i in range(3):
                if sum(grid[r + i][c + j] for j in range(3)) != magic_sum:
                    return False
            for j in range(3):
                if sum(grid[r + i][c + j] for i in range(3)) != magic_sum:
                    return False
            if sum(grid[r + i][c + i] for i in range(3)) != magic_sum:
                return False
            if sum(grid[r + i][c + 2 - i] for i in range(3)) != magic_sum:
                return False
            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic_square(r, c):
                    count += 1
        return count
        
# @lc code=end


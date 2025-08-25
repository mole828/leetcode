#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        y = 0
        x = 0
        target = complex(1, -1)
        res = []
        while y + x < rows + cols - 1:
            next_y = y + int(target.imag)
            next_x = x + int(target.real)
            if 0 <= y < rows and 0 <= x < cols:
                res.append(mat[y][x])
                if not 0 <= next_y < rows:
                    next_x += 1
                    target = -target
                elif not 0 <= next_x < cols:
                    next_y += 1
                    target = -target
            y = next_y
            x = next_x
        return res

# @lc code=end

print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
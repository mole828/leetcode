#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def isSpecial(y: int, x: int):
            for oy in range(len(mat)):
                if oy == y:
                    continue
                if mat[oy][x] == 1:
                    return False
            row = mat[y]
            for ox in range(len(row)):
                if ox == x:
                    continue
                if row[ox] == 1:
                    return False
            return True
        output = 0
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if mat[y][x]==1 and isSpecial(y,x):
                    output += 1
        return output         
# @lc code=end


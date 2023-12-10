#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        for y,row in enumerate(matrix):
            for x,value in enumerate(row):
                output[x][y]=value 
        return output

# @lc code=end
print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))

#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

# @lc code=start
from functools import cache
from typing import List

# Time Limit Exceeded
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rowLength = len(matrix)
        colLength = len(matrix[0])
        count = 0
        for top in range(rowLength):
            for bottom in range(top+1, rowLength+1):
                for left in range(colLength):
                    for right in range(left+1,colLength+1):
                        # print({'top':top,'bottom':bottom,'left':left,'right':right})
                        rows = matrix[top:bottom]
                        subSummay = sum(sum(row[left:right]) for row in rows)
                        if subSummay == target:
                            count += 1
        return count
    
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        @cache
        def sum2(row: int, col: int):
            return matrix[row][col] + (sum2(row,col-1) if col>0 else 0)
        @cache
        def sumL2R(row: int, left: int, right: int):
            return sum2(row, right) - (sum2(row, left) if left!=right else 0)
        count = 0
        for left in range(len(matrix[0])):
            for right in range(left, len(matrix[0])):
                has = {0:1}
                subsum = 0
                for row in range(len(matrix)):
                    subsum += sumL2R(row, left, right)
                    count += has.get(subsum-target, 0)
                    has[subsum] = has.get(subsum,0) + 1
                # print({"left":left,"right":right,"has":has})
        return count 
        
# @lc code=end
    

print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]],0))
print(Solution().numSubmatrixSumTarget([[1,-1],[-1,1]],0))


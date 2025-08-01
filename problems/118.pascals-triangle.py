#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        while len(res) < numRows:
            old_row = res[-1]
            new_row = [0] * (len(old_row) + 1)
            for i,v in enumerate(old_row):
                new_row[i] += v
                new_row[i+1] += v
            res.append(new_row)
        return res
        
# @lc code=end


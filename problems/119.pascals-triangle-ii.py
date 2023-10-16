#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex-1)
        return [1] + [last[i]+last[i+1] for i in range(len(last)-1)] + [1]
# @lc code=end


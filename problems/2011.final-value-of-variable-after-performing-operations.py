#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if s[1] == '+' else -1 for s in operations)

# @lc code=end


#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        return self.climbStairs(n-1)+self.climbStairs(n-2)
# @lc code=end


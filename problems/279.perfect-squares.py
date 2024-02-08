#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from functools import cache


class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        if n==0:
            return 0 
        nn = int(n ** (1/2))
        return min(
            self.numSquares(n-sub**2) for sub in range(nn,0,-1)
        ) + 1
# @lc code=end

print(Solution().numSquares(13))
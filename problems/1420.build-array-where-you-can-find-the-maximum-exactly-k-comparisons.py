#
# @lc app=leetcode id=1420 lang=python3
#
# [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
#

# @lc code=start
from functools import cache

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(last_length: int, max_val: int, cost: int) -> int:
            if last_length == 0:
                return 1 if cost == 0 else 0
            return sum(dp(last_length-1, max(max_val, j), cost - (max_val < j)) for j in range(1, m + 1))
        return dp(n, 0, k) % (10**9 + 7)  
# @lc code=end
print( Solution().numOfArrays(n = 2, m = 3, k = 1) )
print( Solution().numOfArrays(n = 5, m = 2, k = 3) )
print( Solution().numOfArrays(n = 9, m = 1, k = 1) )

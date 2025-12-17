#
# @lc app=leetcode id=3573 lang=python3
# @lcpr version=30204
#
# [3573] Best Time to Buy and Sell Stock V
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
import itertools
from math import inf
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        @cache
        def dp(i: int, k: int) -> int:
            if i == n:
                return 0
            if k == 0:
                return 0
            i_price = prices[i]
            profits = itertools.chain(
                [0, dp(i+1, k)], 
                (abs(i_price - prices[j]) + dp(j+1, k-1) for j in range(i+1, n))
            )
            return max(profits, default=0)
        return dp(0, k)
    def maximumProfit(self, prices: List[int], k: int) -> int:
        f = [[0, -inf, -inf] for _ in range(k + 1)]
        for p in prices:
            for j in range(k, 0, -1):
                f[j][0] = max(f[j][0], f[j][1] + p, f[j][2] - p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
                f[j][2] = max(f[j][2], f[j - 1][0] + p)
        return f[k][0]
# @lc code=end

# print(Solution().maximumProfit([1,7,9,8,2], 2))
print(Solution().maximumProfit([14,6,10,19], 1))

#
# @lcpr case=start
# [1,7,9,8,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [12,16,19,19,8,1,19,13,9]\n3\n
# @lcpr case=end

#


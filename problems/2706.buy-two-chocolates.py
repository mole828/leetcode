#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        cost = sum(prices[:2])
        if cost > money:
            return money
        return money - cost
# @lc code=end


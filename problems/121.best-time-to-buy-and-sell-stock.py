#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        outputs = [0]
        def dp(i: int) -> int:
            if i == length:
                return - float('inf')
            v = prices[i]
            before = dp(i+1)
            outputs[0] = max(outputs[0],before-v)
            return max(v, before)
        dp(0)
        return outputs[0]
# @lc code=end


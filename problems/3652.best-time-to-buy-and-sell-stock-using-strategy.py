#
# @lc app=leetcode id=3652 lang=python3
#
# [3652] Best Time to Buy and Sell Stock using Strategy
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        old_profits = [prices[i]*strategy[i] for i in range(len(prices))]
        max_diff = 0
        for begin in range(len(prices) - k + 1):
            end = begin + k
            half = (begin+end) // 2
            # print(begin, half, end, )
            diff = 0
            for i in range(begin, half):
                diff -= old_profits[i]
            for i in range(half, end):
                diff -= old_profits[i]
                diff += prices[i]
            max_diff = max(max_diff, diff)
        return max_diff + sum(old_profits)
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        left_window: list[tuple[int, int]] = []
        right_window: list[tuple[int, int]] = []
        diff = 0
        def right_in(i: int):
            nonlocal diff
            old_profit = prices[i] * strategy[i]
            diff -= old_profit
            now_profit = prices[i]
            diff += now_profit
            right_window.append((old_profit, now_profit))
        def right_to_left():
            nonlocal diff
            old_profit, now_profit = right_window.pop(0)
            diff -= now_profit
            left_window.append((old_profit, 0))
        def left_pop():
            nonlocal diff
            old_profit, now_profit = left_window.pop(0)
            diff -= now_profit
            diff += old_profit
        half_k = k // 2
        for i in range(k):
            right_in(i)
        for i in range(half_k):
            right_to_left()
        # print(left_window, right_window, diff)
        max_diff = max(diff, 0)
        for i in range(k, len(prices)):
            left_pop()
            right_in(i)
            right_to_left()
            # print(left_window, right_window, diff)
            max_diff = max(max_diff, diff)
        return max_diff + sum(prices[i]*strategy[i] for i in range(len(prices)))

# @lc code=end

if __name__ == "__main__":
    print(Solution().maxProfit([4,2,8], [-1,0,1], 2))
    print(Solution().maxProfit([5,8], [-1, -1], 2))
    print(Solution().maxProfit([4,7,13], [-1, -1,0], 2))
    pass
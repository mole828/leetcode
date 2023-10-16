#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
from bisect import bisect_left
from functools import cache
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i: int):
            if i == len(days):
                return 0
            return min(
                costs[0] + dp(i+1), 
                costs[1] + dp(bisect_left(days, days[i]+7, lo= i)), 
                costs[2] + dp(bisect_left(days, days[i]+30, lo= i))
            )
        return dp(0) 
# @lc code=end

print(Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
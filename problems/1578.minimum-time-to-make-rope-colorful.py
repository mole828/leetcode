#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start
from functools import cache
from typing import List


# Passed, but "Memory Limit Exceeded"
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        length = len(colors)

        @cache
        def dp(last: str, i: int):
            if i==length:
                return 0
            this_color = colors[i]
            return min([
                neededTime[i] + dp(last, i+1),
                dp(this_color, i+1) if last != this_color else float('inf') 
            ])

        return dp('',0)

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        begin = 0
        end = 0
        while end < len(colors):
            while end<len(colors) and colors[end] == colors[begin]:
                end += 1
            sub = neededTime[begin:end]
            cost += sum(sub) - max(sub)
            begin = end
        return cost
# @lc code=end

print(Solution().minCost(colors = "abaac", neededTime = [1,2,3,4,5]))

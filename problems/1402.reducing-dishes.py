#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
from functools import cache
from typing import List

# pass, runtime beats 18.13 %, memory usage beats 7.43 % 
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(index: int, mut: int):
            if index == len(satisfaction):
                return 0
            return max(
                satisfaction[index]*mut + dp(index+1, mut+1),
                dp(index+1, mut),
            )
        return dp(0, 1)
    
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(key=lambda x:-x)
        ans = 0
        for i in range(len(satisfaction)+1):
            dx = sum(satisfaction[:i])
            if dx < 0:
                break 
            ans += dx 
        return ans

# @lc code=end


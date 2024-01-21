#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        @cache
        def dp(i: int)->int:
            return max(
                (dp(ii) 
                for ii in range(
                    i+2, 
                    length
                )), 
                default=0 
            ) + nums[i]
        return max(
            dp(i) for i in range(length)
        )
# @lc code=end


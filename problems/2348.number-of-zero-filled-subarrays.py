#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        for right, x in enumerate(nums):
            if x == 0:
                res += right - left + 1
            else:
                left = right + 1
        return res

        
# @lc code=end


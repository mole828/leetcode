#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(1, length):
            a = nums[i-1]
            b = nums[i] 
            nums[i] = max(b, a+b)
        return max(nums)
# @lc code=end


#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if 0 in nums:
            i0 = nums.index(0)
            return max(
                self.maxProduct(nums[:i0]),
                self.maxProduct(nums[i0+1:]),
                0,
            )
        currentMax = 1
        currentMin = 1
        globalMax = nums[0]
        for v in nums:
            currentMax, currentMin = (
                max(v, currentMax*v, currentMin*v),
                min(v, currentMax*v, currentMin*v),
            )
            globalMax = max(currentMax, globalMax)
        return globalMax
# @lc code=end

print(Solution().maxProduct([-2,0,-1]))
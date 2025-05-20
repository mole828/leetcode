#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    # Time Limit Exceeded, 660/668 cases passed
    def _isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for (left, right) in queries:
            for i in range(left, right + 1):
                nums[i] = max(0 , nums[i] - 1)
        return not any(nums)
    
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for (left, right) in queries:
            diff[left] += 1
            diff[right + 1] -= 1
        for x, sum_d in zip(nums, accumulate(diff)):
            if x > sum_d:
                return False
        return True
        
# @lc code=end


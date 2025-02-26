#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
from typing import List

# Time Limit Exceeded, 32/66 cases passed
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_abs_sum = 0
        for left in range(n):
            for right in range(left, n):
                max_abs_sum = max(max_abs_sum, abs(sum(nums[left:right+1])))
                
        return max_abs_sum
        
# Time Limit Exceeded, 54/66 cases passed
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_abs_sum = 0
        for left in range(n):
            window = 0
            for right in range(left, n):
                window += nums[right]
                max_abs_sum = max(max_abs_sum, abs(window))
                
        return max_abs_sum
    
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = f_max = f_min = 0
        for x in nums:
            f_max = max(f_max, 0) + x
            f_min = min(f_min, 0) + x
            ans = max(ans, f_max, -f_min)
        return ans
# @lc code=end


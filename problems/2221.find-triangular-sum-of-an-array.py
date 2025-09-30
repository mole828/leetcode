#
# @lc app=leetcode id=2221 lang=python3
#
# [2221] Find Triangular Sum of an Array
#

# @lc code=start
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]
        
# @lc code=end


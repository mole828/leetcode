#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
        
# @lc code=end


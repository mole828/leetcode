#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        min_i = nums[0]
        for j in range(1, len(nums)):
            num_j = nums[j]
            if num_j > min_i:
                ans = max(ans, num_j - min_i)
            
            min_i = min(min_i, num_j)
        return ans
        
# @lc code=end


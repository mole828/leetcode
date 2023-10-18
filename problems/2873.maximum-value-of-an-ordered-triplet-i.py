#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        return max([
            (nums[i]-nums[j])*nums[k] 
             for i in range(n) 
             for j in range(i+1, n) 
             for k in range(j+1, n)
        ]+[0])
        

# @lc code=end


#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
from typing import List

#1 2023-10-18
#2 2025-04-02

# O(n^3)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        return max([
            (nums[i]-nums[j])*nums[k] 
             for i in range(n) 
             for j in range(i+1, n) 
             for k in range(j+1, n)
        ]+[0])
    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res

        

# @lc code=end


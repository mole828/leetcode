#
# @lc app=leetcode id=3423 lang=python3
#
# [3423] Maximum Difference Between Adjacent Elements in a Circular Array
#

# @lc code=start
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        rand = nums + nums
        max_diff = 0
        for i in range(len(rand)-1):
            a,b = rand[i], rand[i+1]
            max_diff = max(max_diff, abs(a-b))
        return max_diff

# @lc code=end


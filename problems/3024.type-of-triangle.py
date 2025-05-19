#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        if a + b <= c:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"
        
# @lc code=end


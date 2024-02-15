#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
from functools import cache
from typing import List

# Time Limit Exceeded, 603 / 980 testcases passed
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        length = len(nums)
        @cache
        def isPolygon(perimeters: tuple[int]) -> bool:
            if len(perimeters)<3:
                return False 
            sumOfPerimeters = sum(perimeters)
            for perimeter in perimeters:
                if perimeter >= sumOfPerimeters - perimeter:
                    return False
            return True
        @cache
        def dp(i: int, perimeters: tuple[int]):
            if i == length:
                if isPolygon(perimeters):
                    return sum(perimeters)
                return -1
            return max(
                dp(i+1, perimeters),
                dp(i+1, perimeters + (nums[i],))
            )
        return dp(0,())

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1
# @lc code=end

print(Solution().largestPerimeter([5,5,5]))
print(Solution().largestPerimeter([1,12,1,2,5,50,3]))
print(Solution().largestPerimeter([25,9,470,173,149,179,71,291,478,443,446,204,263,183,188,160,449,229,322,1]))
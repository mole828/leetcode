#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            if nums.count(0) > 1:
                return [0 for _ in nums]
            i0 = nums.index(0)
            v0 = reduce(lambda a,b:a*b, nums[:i0] + nums[i0+1:])
            return [v0 if i==i0 else 0 for i in range(len(nums))]

        product = reduce(lambda a,b:a*b, nums)
        return [
            product//num for num in nums
        ]
# @lc code=end

print(Solution().productExceptSelf([1,2,0,1]))
#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        has = nums.count(target)
        if has < 1:
            return [-1,-1]
        a = nums.index(target)
        b = a + has - 1
        return [a,b]

# @lc code=end

print(Solution().searchRange([5,7,7,8,8,10], 8))
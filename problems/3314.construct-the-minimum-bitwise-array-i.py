#
# @lc app=leetcode id=3314 lang=python3
#
# [3314] Construct the Minimum Bitwise Array I
#

# @lc code=start
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            if x == 2:
                nums[i] = -1
            else:
                t = ~x
                nums[i] ^= (t & -t) >> 1
        return nums
# @lc code=end


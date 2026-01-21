#
# @lc app=leetcode id=3315 lang=python3
#
# [3315] Construct the Minimum Bitwise Array II
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


#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
#

# @lc code=start
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + x) % n] for i, x in enumerate(nums)]

# @lc code=end


#
# @lc app=leetcode id=3202 lang=python3
#
# [3202] Find the Maximum Length of Valid Subsequence II
#

# @lc code=start
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mat = [[0]*k for _ in range(k)]
        for x in nums:
            x_mod_k = x % k
            for y, v in enumerate(mat[x_mod_k]):
                mat[y][x_mod_k] = v + 1
        return max(map(max, mat))
# @lc code=end


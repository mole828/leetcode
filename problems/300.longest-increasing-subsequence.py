#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        @cache
        def dp(i: int)->int:
            m = max(
                (dp(j) for j in range(i,length) if nums[j]>nums[i]),
                default=0
            ) + 1
            # print(f"dp({i}): {m}")
            return m 
        return max(dp(i) for i in range(length))
# @lc code=end

print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
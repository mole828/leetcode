#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        set_of_nums = set(nums)
        for left in range(n):
            set_of_window = set()
            for right in range(left, n):
                set_of_window.add(nums[right])
                if set_of_window == set_of_nums:
                    ans += n - right
                    break
        return ans

# @lc code=end


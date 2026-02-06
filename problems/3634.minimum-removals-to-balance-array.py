#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#

# @lc code=start
from typing import List

from numpy import inf


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        last = 0
        max_val_index = 0
        max_val = nums[0]
        for min_val_index, min_val in enumerate(nums):
            while max_val <= min_val * k :
                max_val_index += 1
                max_val = nums[max_val_index] if max_val_index < n else inf
            window_size = max_val_index - min_val_index
            last = max(last, window_size)                

        return n - last
        
# @lc code=end


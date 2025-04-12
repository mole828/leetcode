#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set(nums)
        min_num = min(s)
        if k > min_num:
            return -1
        return len(s) - (k == min_num)
        
# @lc code=end


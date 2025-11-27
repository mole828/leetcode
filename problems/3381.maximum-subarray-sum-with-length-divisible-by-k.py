#
# @lc app=leetcode id=3381 lang=python3
#
# [3381] Maximum Subarray Sum With Length Divisible by K
#

# @lc code=start
from itertools import accumulate
from math import inf
from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre = list(accumulate(nums, initial=0))
        min_s = [inf] * k
        ans = -inf
        for j, s in enumerate(pre):
            i = j % k
            ans = max(ans, s - min_s[i])
            min_s[i] = min(min_s[i], s)
        return ans
            
# @lc code=end


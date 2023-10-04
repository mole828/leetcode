#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        has = defaultdict(int)
        for num in nums:
            ans += has[num]
            has[num] += 1
        return ans

# @lc code=end


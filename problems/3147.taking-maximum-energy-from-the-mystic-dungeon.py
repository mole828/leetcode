#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0
            take = energy[i] + dp(i + k)
            # skip = dp(i + 1)
            # return max(take, skip)
            return take
        return max(
            dp(i) for i in range(n)
        )
# @lc code=end

print(Solution().maximumEnergy(
    [5,2,-10,-5,1], 3
))
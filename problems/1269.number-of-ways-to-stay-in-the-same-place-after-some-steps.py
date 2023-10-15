#
# @lc app=leetcode id=1269 lang=python3
#
# [1269] Number of Ways to Stay in the Same Place After Some Steps
#

# @lc code=start
from functools import cache

class Solution:
    mod = 10 ** 9 + 7
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(place: int, step: int):
            if place < 0 or place == arrLen:
                return 0 
            if step == 0:
                return 1 if place == 0 else 0
            return sum([
                dp(place+1, step-1),
                dp(place, step-1),
                dp(place-1, step-1),
            ])
        return dp(0, steps) % self.mod

# @lc code=end
if __name__ == '__main__':
    print(Solution().numWays(steps=3, arrLen=2))

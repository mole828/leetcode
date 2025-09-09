#
# @lc app=leetcode id=2327 lang=python3
#
# [2327] Number of People Aware of a Secret
#

# @lc code=start
import heapq
from typing import List, Tuple


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        known = [0] * (n+1)
        known[1] = 1
        for i in range(1, n+1):
            known[i] %= MOD
            for j in range(i+delay, min(i+forget, n+1)):
                known[j] += known[i]
        return sum(known[-forget:]) % MOD

# @lc code=end

print(Solution().peopleAwareOfSecret(6, 2, 4))
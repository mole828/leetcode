#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        length = len(jobDifficulty)
        # print(f"length: {length}")
        if d>length:
            return -1
        @cache
        def dp(i: int, last: int) -> int:
            # print(f"dp({i},{last})")
            if last==0:
                return 0 if i==length else float('inf')
            ls = [
                max(jobDifficulty[i:j], default=0)+dp(j, last-1) 
                for j in range(i+1, length+1)
            ]
            # print(f"dp({i},{last}), {ls}")
            return min(ls, default=float('inf'))
        return dp(0, d)
# @lc code=end

print(Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
print(Solution().minDifficulty(jobDifficulty = [9,9,9], d = 4))
print(Solution().minDifficulty(jobDifficulty = [1,1,1], d = 3))
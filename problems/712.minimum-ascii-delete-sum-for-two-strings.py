#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n and j == m:
                return 0
            if i == n:
                return sum(ord(s2[k]) for k in range(j, m))
            if j == m:
                return sum(ord(s1[k]) for k in range(i, n))

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)
            else:
                delete_s1 = ord(s1[i]) + dfs(i + 1, j)
                delete_s2 = ord(s2[j]) + dfs(i, j + 1)
                return min(delete_s1, delete_s2)
        return dfs(0, 0)
# @lc code=end


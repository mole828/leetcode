#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#

# @lc code=start
from functools import cache

MODULO = 10 ** 9 + 7

# Memory Limit Exceeded, 1502/1502 cases passed
# 1502/1502 cases passed?
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        nums = [
            i**x for i in reversed(range(1, int(n**(1/x)) + 2))
        ]
        print(nums)
        @cache
        def dfs(i: int, need: int) -> int:
            if need == 0:
                return 1
            if need < 0:
                return 0
            if i == len(nums):
                return 0
            # pick
            pick = dfs(i + 1, need - nums[i])
            # not pick
            not_pick = dfs(i + 1, need)
            return (pick + not_pick) % MODULO
        return dfs(0, n)


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        f = [1] + [0] * n
        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break
            for s in range(n, v - 1, -1):
                f[s] += f[s - v]
            # print(f)
        return f[n] % MODULO
# @lc code=end

# print(Solution().numberOfWays(10, 2))
print(Solution().numberOfWays(64, 3))
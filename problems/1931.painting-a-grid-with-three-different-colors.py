#
# @lc app=leetcode id=1931 lang=python3
# @lcpr version=30204
#
# [1931] Painting a Grid With Three Different Colors
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # m in 1..5
        # n in 1..1000
        next_dict: dict[tuple, set[tuple]] = {}
        def f(arr: list[int] = []):
            if len(arr) == m:
                next_dict[tuple(arr)] = set()
                return
            for i in range(3):
                if arr and arr[-1] == i:
                    continue
                f(arr + [i])
        f()
        print(next_dict)
        for last in next_dict.keys():
            for next in next_dict.keys():
                if any(x == y for x, y in zip(last, next)):
                    continue
                next_dict[last].add(next)
        print(next_dict)
        MOD = 10**9 + 7
        @cache
        def dfs(last_layer: tuple, last_deep: int) -> int:
            if last_deep == 0:
                return 1
            ans = 0
            for next in next_dict[last_layer]:
                ans += dfs(next, last_deep - 1)
            return ans % MOD
        return sum(dfs(last, n - 1) for last in next_dict.keys()) % MOD
# @lc code=end

print(Solution().colorTheGrid(m = 1, n = 2))

#
# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 5\n5\n
# @lcpr case=end

#


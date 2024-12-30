#
# @lc app=leetcode id=2466 lang=python3
# @lcpr version=
#
# [2466] Count Ways To Build Good Strings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return 1
            return (dfs(i - zero) + dfs(i - one)) % MOD
        return sum(dfs(i) for i in range(low, high + 1)) % MOD
        
# @lc code=end

print(Solution().countGoodStrings(3, 3, 1, 1))

#
# @lcpr case=start
# 3\n3\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n3\n1\n2\n
# @lcpr case=end

#


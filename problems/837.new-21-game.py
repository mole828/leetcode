#
# @lc app=leetcode id=837 lang=python3
# @lcpr version=30204
#
# [837] New 21 Game
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        @cache
        def dfs(i: int) -> float:
            if i >= k:
                return float(i<=n)
            if i == k - 1:
                return min(n-k+1, maxPts) / maxPts
            return dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts

        return dfs(0)
# @lc code=end

# print(Solution().new21Game(10, 1, 10))
# print(Solution().new21Game(6, 1, 10))
print(Solution().new21Game(21, 17, 10))

#
# @lcpr case=start
# 10\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 6\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 21\n17\n10\n
# @lcpr case=end

#


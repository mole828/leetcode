#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#

# @lc code=start
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75))
        
        if n >= 4800:
            return 1
        return dfs(n, n)
# @lc code=end


#
# @lc app=leetcode id=2435 lang=python3
#
# [2435] Paths in Matrix Whose Sum Is Divisible by K
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        MOD = 10**9 + 7
        @cache
        def dfs(y: int, x: int, mod_need: int) -> int:
            if y == rows - 1 and x == cols - 1:
                return 1 if (mod_need - grid[y][x]) % k == 0 else 0
            ans = 0
            for dy, dx in [(0, 1), (1, 0)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols:
                    mod_need_next = (mod_need - grid[y][x]) % k
                    ans += dfs(ny, nx, mod_need_next)
            return ans % MOD
        return dfs(0, 0, k)

# @lc code=end

print(Solution().numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3))  # Expected output: 2
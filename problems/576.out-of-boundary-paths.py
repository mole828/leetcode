#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
from functools import cache


class Solution:
    MOD = 10 ** 9 + 7
    @cache
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        out = not (0<=startRow<m and 0<=startColumn<n)
        if out:
            return 1
        if maxMove == 0:
            return 0
        ans = sum(
            self.findPaths(m,n,maxMove-1,startRow+dy,startColumn+dx) for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]
        )
        # print(f"findPaths({m},{n},{maxMove}, {startRow}, {startColumn}): {ans}")
        return ans % Solution.MOD
# @lc code=end

print(Solution().findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
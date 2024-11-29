#
# @lc app=leetcode id=2577 lang=python3
# @lcpr version=
#
# [2577] Minimum Time to Visit a Cell In a Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappop, heappush
from typing import List

from numpy import inf


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while True:
            d, i, j = heappop(h)
            if d > dis[i][j]: continue
            if i == m - 1 and j == n - 1:
                return d
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # 枚举周围四个格子
                if 0 <= x < m and 0 <= y < n:
                    nd = max(d + 1, grid[x][y])
                    nd += (nd - x - y) % 2
                    if nd < dis[x][y]:
                        dis[x][y] = nd
                        heappush(h, (nd, x, y))
        
# @lc code=end



#
# @lcpr case=start
# [[0,1,3,2],[5,1,2,5],[4,3,8,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2,4],[3,2,1],[1,0,4]]\n
# @lcpr case=end

#


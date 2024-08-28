#
# @lc app=leetcode id=1905 lang=python3
# @lcpr version=
#
# [1905] Count Sub Islands
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
from typing import List

import numpy as np


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def bfs(sx: int, sy: int) -> int:
            q = deque([(sx, sy)])
            grid2[sx][sy] = 0
            # 判断岛屿包含的每一个格子是否都在 grid1 中出现了
            check = (grid1[sx][sy] == 1)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                        q.append((nx, ny))
                        grid2[nx][ny] = 0
                        if grid1[nx][ny] != 1:
                            check = False
            
            return int(check)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += bfs(i, j)
        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]\n[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]\n
# @lcpr case=end

#


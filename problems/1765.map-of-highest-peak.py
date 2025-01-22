#
# @lc app=leetcode id=1765 lang=python3
# @lcpr version=
#
# [1765] Map of Highest Peak
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        res = [[-1] * m for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    res[i][j] = 0
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            new_q = []
            for i, j in q:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and res[x][y] == -1:
                        res[x][y] = res[i][j] + 1
                        new_q.append((x, y))
            q = new_q
        return res
        
# @lc code=end



#
# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1],[1,0,0],[0,0,0]]\n
# @lcpr case=end

#


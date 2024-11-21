#
# @lc app=leetcode id=2257 lang=python3
# @lcpr version=
#
# [2257] Count Unguarded Cells in the Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


# Time Limit Exceeded, 38 / 48 testcases passed
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(m)]
        for x, y in walls:
            mat[x][y] = 2
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for gx, gy in guards:
            mat[gx][gy] = 2
            for dx, dy in directions:
                x, y = gx, gy
                while 0 <= x + dx < m and 0 <= y + dy < n and mat[x + dx][y + dy] != 2:
                    mat[x + dx][y + dy] = 1
                    x += dx
                    y += dy
        return sum(row.count(0) for row in mat)

# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/solutions/6067031/beats-100-simple-and-easy-i-guess-list-most-common-array-interview-problems/
# 为什么我的超时 他这个代码能过呢

# @lc code=end



#
# @lcpr case=start
# 4\n6\n[[0,0],[1,1],[2,3]]\n[[0,1],[2,2],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[1,1]]\n[[0,1],[1,0],[2,1],[1,2]]\n
# @lcpr case=end

#


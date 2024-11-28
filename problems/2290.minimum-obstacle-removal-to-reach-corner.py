#
# @lc app=leetcode id=2290 lang=python3
# @lcpr version=
#
# [2290] Minimum Obstacle Removal to Reach Corner
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        visited = set()
        que = SortedList([(0, 0, 0)])
        while que:
            break_count, y, x = que.pop(0)
            if (y, x) in visited:
                continue
            visited.add((y, x))
            print(break_count, y, x)
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return break_count
            for dy, dx in [(0,-1), (0,1), (-1,0), (1,0)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                    if grid[ny][nx] == 1:
                        que.add((break_count + 1, ny, nx))
                    if grid[ny][nx] == 0:
                        que.add((break_count, ny, nx))


# @lc code=end

print(Solution().minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))

#
# @lcpr case=start
# [[0,1,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]\n
# @lcpr case=end

#


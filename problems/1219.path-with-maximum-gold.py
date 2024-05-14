#
# @lc app=leetcode id=1219 lang=python3
# @lcpr version=
#
# [1219] Path with Maximum Gold
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        base_mask = 0
        def to_mask(y: int, x: int) -> int:
            return 1 << (y*cols + x)
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    base_mask |= to_mask(row, col)
        def next_step(y: int, x: int) -> list[tuple[int,int]]:
            step = []
            for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ty = y+dy 
                tx = x+dx 
                if not 0<=ty<rows:
                    continue
                if not 0<=tx<cols:
                    continue
                step.append((ty,tx))
            return step
        def dfs(y: int, x: int, mask: int) -> int:
            this_mask = to_mask(y,x)
            if mask & this_mask:
                return 0
            new_mask = mask | this_mask
            return grid[y][x] + max(dfs(yy,xx,new_mask) for yy,xx in next_step(y,x))
        return max( dfs(y,x,base_mask) for y in range(rows) for x in range(cols) )
# @lc code=end

print(Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))

#
# @lcpr case=start
# [[0,6,0],[5,8,7],[0,9,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]\n
# @lcpr case=end

#


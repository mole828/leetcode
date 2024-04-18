#
# @lc app=leetcode id=463 lang=python3
# @lcpr version=
#
# [463] Island Perimeter
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        def round(yx: tuple[int,int]) -> set[tuple[int,int]]:
            y,x = yx 
            rounds = set()
            for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ty,tx = y+dy,x+dx
                ty = max(0,min(ty,rows-1))
                tx = max(0,min(tx,cols-1))
                rounds.add((ty,tx))
            if yx in rounds:
                rounds.remove(yx)
            return rounds
        perimeter = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x]:
                    last = 4
                    for ty,tx in round((y,x)):
                        if grid[ty][tx]:
                            last -= 1
                    perimeter += last 
        return perimeter

# @lc code=end



#
# @lcpr case=start
# [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0]]\n
# @lcpr case=end

#


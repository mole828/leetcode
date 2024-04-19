#
# @lc app=leetcode id=200 lang=python3
# @lcpr version=
#
# [200] Number of Islands
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        arrival = set()
        def diffusion(yx: tuple[int,int], i: int) -> int:
            # print(yx,i)
            y,x = yx 
            if not 0<=y<len(grid):
                return 0
            if not 0<=x<len(grid[y]):
                return 0
            if grid[y][x]=='1' and yx not in arrival:
                arrival.add(yx)
                for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ty,tx = y+dy,x+dx 
                    diffusion((ty,tx),i)
                return i
            return 0
        lands = 0
        for y,row in enumerate(grid):
            for x,_ in enumerate(row):
                lands = max(lands, diffusion((y,x),lands+1))
        return lands
            
        
# @lc code=end

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#


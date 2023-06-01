from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:return -1
        n = len(grid)
        que = [(0,0,1)]
        grid[0][0] = 1

        while que:
            y,x,l = que.pop(0)
            if y == x == n-1: return l 
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if dy==dx==0:continue
                    ty, tx = y+dy, x+dx 
                    if 0<=ty<n and 0<=tx<n and not grid[ty][tx]:
                        grid[ty][tx] = 1
                        que.append((ty,tx,l+1))
        
        return -1
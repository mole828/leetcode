from typing import List


class Solution:
    def largest1BorderedSquare(self,  grid: List[List[int]]) -> int:
        def check(p, l):
            for i in range(l): 
                if grid[p[0]][p[1]+i] == 0 or grid[p[0]+l-1][p[1]+i] == 0: return False
                if grid[p[0]+i][p[1]] == 0 or grid[p[0]+i][p[1]+l-1] == 0: return False
            return True
        
        for l in range(min(len(grid[0]), len(grid)), -1, -1):
            for y in range(len(grid[0])-l+1):
                for x in range(len(grid)-l+1):
                    if check([x, y], l): return l**2 
        return 0
    
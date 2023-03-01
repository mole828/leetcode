from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [
                max(
                    grid[y+dy][x+dx] 
                    for dx in range(3) 
                    for dy in range(3)
                ) for x in range(len(grid[y])-2)
            ] for y in range(len(grid)-2)
        ]
            
                
                    

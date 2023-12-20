from itertools import product
from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def min_total_distance(self, grid: List[List[int]]) -> int:
        # Write your code here
        nRows = len(grid)
        nCols = len(grid[0])
        cost_matrix = [[0]*nCols for _ in range(nRows)]
        for y,row in enumerate(grid):
            for x,value in enumerate(row):
                if value:
                    for targetY,targetRow in enumerate(cost_matrix):
                        dy = abs(targetY-y)
                        for targetX in range(nCols):
                            dx = abs(targetX-x)
                            targetRow[targetX] += dy+dx 
        # print(cost_matrix)
        return min(min(row) for row in cost_matrix)
    
    def min_total_distance(self, grid: List[List[int]]) -> int:
        points: list[tuple[y,x]] = []
        for y,row in enumerate(grid):
            for x,value in enumerate(row):
                if value:
                    points.append((y,x))
        ySum = 0
        xSum = 0
        for y,x in points:
            ySum += y
            xSum += x 
        y = ySum//len(points)
        x = xSum//len(points)
        output = float('inf')
        for dy,dx in product([-1,0,1],[-1,0,1]):
            ty = y+dy
            tx = x+dx 
            cost = 0
            for py,px in points:
                cost += abs(py-ty)+abs(px-tx)
            output = min(output,cost)
        return output 



if __name__ == '__main__':
    print(Solution().min_total_distance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
    print(Solution().min_total_distance([[1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]]))
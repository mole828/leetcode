from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0 
        for row in grid:
            for x in row:
                if x<0:
                    ans+=1
        return ans
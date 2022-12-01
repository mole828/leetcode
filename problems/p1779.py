from typing import List
import numpy

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best, ans = numpy.Inf, -1
        for i, [px,py] in enumerate(points):
            if px == x or py == y:
                dl = abs(px-x)+abs(py-y)
                if dl < best:
                    best, ans = dl, i 
        return ans
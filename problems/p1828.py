from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [
            len([1 for (yp,xp) in points if ((y-yp)**2+(x-xp)**2)**0.5<=r]) for (y,x,r) in queries
        ]
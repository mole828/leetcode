#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
from functools import cache, reduce
from typing import List
import math

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        @cache
        def d(a:int, b:int)->float:
            pa,pb = points[a], points[b]
            dx,dy = abs(pa[0]-pb[0]), abs(pa[1]-pb[1])
            return max(dx,dy)
        if len(points)==2:
            return d(0,1)
        endMask = sum(1<<i for i in range(len(points)))
        @cache
        def dp(mask: int, index: int) -> int:
            # print(mask)
            indexMask = 1<<index 
            if mask==endMask:
                # print(mask)
                return 0
            if mask & indexMask:
                return math.inf
            newMask = mask | indexMask
            return min(dp(newMask,i)+d(index,i) for i in range(len(points)) if i!=index)
        return min(dp(0,i) for i in range(len(points)))
    
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        c=0
        for i in range(len(points)-1):
            c+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
        return c
# @lc code=end

if __name__ == "__main__":
    # print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
    print(Solution().minTimeToVisitAllPoints([[3,2],[-2,2]]))
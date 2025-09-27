#
# @lc app=leetcode id=812 lang=python3
# @lcpr version=30204
#
# [812] Largest Triangle Area
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    res = max(res, self.triangleArea(points[i], points[j], points[k]))
        return res
    
    def triangleArea(self, p1: List[int], p2: List[int], p3: List[int]) -> float:
        return 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0])
        
# @lc code=end



#
# @lcpr case=start
# [[0,0],[0,1],[1,0],[0,2],[2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0],[0,0],[0,1]]\n
# @lcpr case=end

#


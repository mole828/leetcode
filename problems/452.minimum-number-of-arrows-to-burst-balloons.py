#
# @lc app=leetcode id=452 lang=python3
# @lcpr version=
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        right = points[0][1]
        arrows = 1
        for a,b in points[1:]:
            if a > right:
                arrows += 1
                right = b 
            else:
                right = min(b, right)
        return arrows
# @lc code=end



#
# @lcpr case=start
# [[10,16],[2,8],[1,6],[7,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4],[5,6],[7,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=3516 lang=python3
#
# [3516] Find Closest Person
#

# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx < dy:
            return 1
        elif dx > dy:
            return 2
        else:
            return 0
# @lc code=end


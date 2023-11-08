#
# @lc app=leetcode id=2849 lang=python3
#
# [2849] Determine if a Cell Is Reachable at a Given Time
#

# @lc code=start
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy:
            if t==1:
                return False
        dx = abs(sx-fx) 
        dy = abs(sy-fy) 
        low = max(dx, dy) 
        return low <= t
# @lc code=end


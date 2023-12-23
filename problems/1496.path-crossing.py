#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dmap: dict[str, tuple[int,int]] = {
            "N": (1,0),
            "S": (-1,0),
            "E": (0,1),
            "W": (0,-1),
        }
        has: set[tuple[int,int]] = set([(0,0)])
        y,x = 0,0
        for char in path:
            dy,dx = dmap[char]
            y += dy 
            x += dx 
            tup = (y,x)
            if tup in has:
                return True
            has.add(tup)
        return False
# @lc code=end


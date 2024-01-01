#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gg = SortedList(g)
        ss = SortedList(s)
        while gg and ss:
            p = ss.pop(0)
            if p >= gg[0]:
                gg.pop(0)
        return len(g)-len(gg)
    
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        iterS = s.__iter__()
        count = len(g)
        for child in g:
            for cookie in iterS:
                if cookie >= child:
                    break
            else:
                count -= 1
        return count
    
# @lc code=end
    
print(Solution().findContentChildren(g = [1,2,3], s = [1,1]))


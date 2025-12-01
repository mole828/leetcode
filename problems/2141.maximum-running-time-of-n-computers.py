#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
from typing import List
import heapq

# link: https://leetcode.cn/problems/maximum-running-time-of-n-computers/solutions/1214440/liang-chong-jie-fa-er-fen-da-an-pai-xu-t-grd8/
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries) // n + 1
        while l + 1 < r:
            x = (l + r) // 2
            if n * x <= sum(min(b, x) for b in batteries):
                l = x
            else:
                r = x
        return l
        
# @lc code=end

print(Solution().maxRunTime(2, [3,3,3]))
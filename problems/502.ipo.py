#
# @lc app=leetcode id=502 lang=python3
# @lcpr version=
#
# [502] IPO
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        last_projects = list(zip(capital, profits))
        heapq.heapify(last_projects)
        ready2go = []
        while k:
            while last_projects:
                cap, profit = heapq.heappop(last_projects)
                if cap <= w:
                    heapq.heappush(ready2go, (-profit))
                else:
                    heapq.heappush(last_projects, (cap,profit))
                    break
            if not ready2go:
                return w
            nag_profit = heapq.heappop(ready2go)
            w -= nag_profit
            k -= 1
        return w
# @lc code=end

print(Solution().findMaximizedCapital(2,0,[1,2,3,],[0,1,1,]))

#
# @lcpr case=start
# 2\n0\n[1,2,3]\n[0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 3\n0\n[1,2,3]\n[0,1,2]\n
# @lcpr case=end

#


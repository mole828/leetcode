#
# @lc app=leetcode id=2285 lang=python3
# @lcpr version=
#
# [2285] Maximum Total Importance of Roads
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        road2 = [0]*n
        for a,b in roads:
            road2[a]+=1
            road2[b]+=1
        return sum(i*v for i,v in enumerate(sorted(road2),start=1))
# @lc code=end



#
# @lcpr case=start
# 5\n[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,3],[2,4],[1,3]]\n
# @lcpr case=end

#


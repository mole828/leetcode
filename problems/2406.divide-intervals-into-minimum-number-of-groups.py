#
# @lc app=leetcode id=2406 lang=python3
# @lcpr version=
#
# [2406] Divide Intervals Into Minimum Number of Groups
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        times = [0] * 1000002
        for a,b in intervals:
            times[a] += 1
            times[b+1] -= 1
        for i in range(1, len(times)):
            times[i] += times[i-1]
        return max(times)
        
# @lc code=end



#
# @lcpr case=start
# [[5,10],[6,8],[1,5],[2,3],[1,10]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,6],[8,10],[11,13]]\n
# @lcpr case=end

#


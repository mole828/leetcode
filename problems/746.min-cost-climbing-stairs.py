#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost + [0]
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[-1]
# @lc code=end


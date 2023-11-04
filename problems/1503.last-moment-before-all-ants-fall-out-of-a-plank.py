#
# @lc app=leetcode id=1503 lang=python3
#
# [1503] Last Moment Before All Ants Fall Out of a Plank
#

# @lc code=start
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))
# @lc code=end


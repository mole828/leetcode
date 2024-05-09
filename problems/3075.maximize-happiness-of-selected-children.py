#
# @lc app=leetcode id=3075 lang=python3
# @lcpr version=
#
# [3075] Maximize Happiness of Selected Children
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        summary = 0
        happiness.sort()
        sub = 0
        while k and happiness:
            summary += max(0, happiness.pop() - sub)
            sub += 1
            k -= 1
        return summary

# @lc code=end


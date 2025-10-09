#
# @lc app=leetcode id=3494 lang=python3
#
# [3494] Find the Minimum Amount of Time to Brew Potions
#

# @lc code=start
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        last_finish = [0] * n
        for m in mana:
            sum_t = 0
            for x, last in zip(skill, last_finish):
                sum_t = max(sum_t, last) + x * m
            last_finish[-1] = sum_t
            for i in range(n - 2, -1, -1):
                last_finish[i] = last_finish[i + 1] - skill[i + 1] * m
        return last_finish[-1]

# @lc code=end

print(Solution().minTime([1,5,2,4],[5,1,4,2]))
# print(Solution().minTime([1,2,3,4],[1,2]))
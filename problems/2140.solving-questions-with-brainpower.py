#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def mostPoints(self, questions: List[tuple[int, int]]) -> int:
        n = len(questions)
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            points, brainpower = questions[i]
            return max(dfs(i+1), dfs(i+1+brainpower)+points)
        return dfs(0)
        
# @lc code=end

print(Solution().mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))

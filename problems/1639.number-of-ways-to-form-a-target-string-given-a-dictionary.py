#
# @lc app=leetcode id=1639 lang=python3
# @lcpr version=30204
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mat: List[Counter[int]] = [Counter(row) for row in zip(*words)]
        @cache
        def dp(i: int = 0, j: int = 0) -> int:
            # print(i, j)
            if j == len(target):
                return 1
            if i == len(mat):
                return 0
            pick = dp(i + 1, j + 1) * (mat[i][target[j]])
            skip = dp(i + 1, j)
            return pick + skip
        
        return dp() % (10**9 + 7)
        
# @lc code=end

print(Solution().numWays(["acca","bbbb","caca"], "aba"))
print(Solution().numWays(["abba","baab"], "bab"))

#
# @lcpr case=start
# ["acca","bbbb","caca"]\n"aba"\n
# @lcpr case=end

# @lcpr case=start
# ["abba","baab"]\n"bab"\n
# @lcpr case=end

#


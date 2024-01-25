#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start

from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i==0 or j==0:
                return 0
            if text1[i-1] == text2[j-1]:
                return dp(i-1,j-1)+1
            else:
                return max(dp(i-1,j),dp(i,j-1))
        return dp(len(text1),len(text2))
# @lc code=end

a = set(['a'])
b = set(['b','c'])
print(a,b, a & b)

print(Solution().longestCommonSubsequence('abcde', 'ace'))
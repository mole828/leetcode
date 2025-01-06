#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from functools import cache

# Time Limit Exceeded
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        @cache
        def dp(i: int = 0, pick: str = '') -> set[str]:
            # print(f"pick: {pick}")
            if len(pick)==3:
                if list(pick) == list(reversed(pick)):
                    # print(f"find: {pick}")
                    return {pick}
                return set()
            if i==len(s):
                return set()
            c = s[i]
            return dp(i+1, pick) | dp(i+1, pick+c)
        return len(dp())
            

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        index = defaultdict(set)
        for i,c in enumerate(s):
            index[c].add(i)
        ans = 0
        for c in index:
            a,b = min(index[c]), max(index[c])
            ans += len(set(s[a+1:b])) 
        return ans

# 2025-01-04 第二次遇到

# @lc code=end


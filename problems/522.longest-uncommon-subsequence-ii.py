#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
from typing import List

def isSubsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s:-len(s))
        for i, word in enumerate(strs):
            if all(not isSubsequence(word,strs[j]) for j in range(len(strs)) if i!=j):
                return len(word)
        return -1

# @lc code=end


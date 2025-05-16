#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        @cache
        def dfs(i: int) -> List[tuple[int, int, str]]:
            if i == len(words):
                return []
            group = groups[i]
            word = words[i]
            tup = (i, group, word)
            longest = [tup]
            for j in range(i + 1, len(words)):
                if groups[j] == group:
                    continue
                sub = [tup] + dfs(j) 
                if len(sub) > len(longest):
                    longest = sub
            return longest
        
        ans = []
        for i in range(len(words)):
            sub = dfs(i)
            # print(sub, i)
            if len(sub) > len(ans):
                ans = sub

        return [w for _, _, w in ans]
        
# @lc code=end

print(Solution().getLongestSubsequence(["c"],[0]))
print(Solution().getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1]))
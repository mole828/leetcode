#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def distance(w0: str, w1: str) -> int:
            return sum(1 for a, b in zip(w0, w1) if a != b)
        @cache
        def dfs(i: int) -> List[str]:
            if i == len(words):
                return []
            group = groups[i]
            word = words[i]
            longest = []
            for j in range(i + 1, len(words)):
                if groups[j] == group:
                    continue
                other = words[j]
                if len(other) != len(word):
                    continue
                if distance(word, other) != 1:
                    continue
                sub = dfs(j)
                if len(sub) > len(longest):
                    longest = sub
            return [word] + longest
        longest = []
        for i in range(len(words)):
            sub = dfs(i)
            if len(sub) > len(longest):
                longest = sub
        return longest
        
# @lc code=end

print(Solution().getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2]))
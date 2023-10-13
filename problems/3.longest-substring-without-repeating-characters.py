#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':return 0
        has: Counter[str] = Counter()
        lr: list[int,int] = [0, 0]
        def hasin():
            has[s[lr[-1]]] += 1
            lr[-1] += 1
        def hasout():
            has[s[lr[0]]] -= 1
            lr[0] += 1
        def sub()->str:
            return s[lr[0]:lr[-1]]
        def repeat()->bool:
            for c, t in has.most_common(1):
                if t>1:
                    return True
            return False
        while lr[-1]<len(s):
            if repeat():
                hasin()
                hasout()
            else:
                hasin()
            # print(sub(), lr, has)
        return lr[-1] - lr[0] - (1 if repeat() else 0)
# @lc code=end

print(Solution().lengthOfLongestSubstring(' '))


#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter
from functools import cache


# Time Limit Exceeded, 233 / 267 testcases passed
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        @cache
        def countBefore(i: int) -> Counter[str]:
            return Counter(s[i:])
        min_window = s
        target = Counter(t)
        if len(target - countBefore(0)):
            return ''
        for i in range(len(s)):
            ci = countBefore(i)
            for j in range(i+1, len(s)+1):
                cj = countBefore(j)
                cSub = ci - cj 
                # print(s[i:j], cSub)
                if len(target-cSub)==0:
                    if j-i < len(min_window):
                        min_window = s[i:j]
        return min_window



# Time Limit Exceeded, 247 / 267 testcases passed
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t) 
        source = Counter(s) 
        if len(target-source):
            return ''
        min_window = [s] 
        @cache
        def dp(left: int, right: int):
            # print(source, s[left:right])
            if right-left < len(t):
                return
            sub = s[left:right]
            # print(sub, source)
            if len(target-source):
                return 
                
            if len(sub) < len(min_window[0]):
                min_window[0] = sub 

            source[s[left]] -= 1
            dp(left+1, right) 
            source[s[left]] += 1

            source[s[right-1]] -= 1
            dp(left, right-1)
            source[s[right-1]] += 1
             
        dp(0, len(s))
        return min_window[0]
    

# Accepted
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        source = Counter(s) 
        target = Counter(t) 
        if len(target-source):
            return ''
        cSub = Counter() 
        left, right = 0, 0
        min_window = s 
        while right < len(s):
            cSub[s[right]] += 1
            # print(right, cSub)
            right += 1
            while len(target-cSub)==0:
                sub = s[left:right]
                # print(min_window, cSub)
                if len(min_window) > len(sub):
                    min_window = sub 
                cSub[s[left]] -= 1
                left += 1
        return min_window
# @lc code=end

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution().minWindow(s = "ab", t = "a"))
print(Solution().minWindow(s = "cabwefgewcwaefgcf", t = "cae"))
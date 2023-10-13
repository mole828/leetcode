#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> int:
        def expand(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        ans = ''
        for i in range(len(s)):
            sub = expand(i,i)
            if len(sub) > len(ans):
                ans = sub
            sub = expand(i, i+1)
            if len(sub) > len(ans):
                ans = sub 
        return ans

# @lc code=end


#
# @lc app=leetcode id=214 lang=python3
# @lcpr version=
#
# [214] Shortest Palindrome
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        r_s = s[::-1]
        for i in range(n):
            if r_s[i:] == s[:n-i]:
                return r_s[:i]+s 
        return ""
# @lc code=end



#
# @lcpr case=start
# "aacecaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

#


#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
def isPalindrome(s) -> bool:
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []
        for left in range(len(s)):
            for right in range(left+1,len(s)+1):
                sub = s[left:right]
                # print(sub, isPalindrome(sub))
                if isPalindrome(sub):
                    palindromes.append(sub)
        return len(palindromes)
# @lc code=end

print(Solution().countSubstrings('abc'))

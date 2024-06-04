#
# @lc app=leetcode id=409 lang=python3
# @lcpr version=
#
# [409] Longest Palindrome
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        count: dict[str, int] = dict()
        for char in s:
            c = count.get(char)
            if not c:
                c = 0
            c += 1
            if c == 2:
                c = 0
                longest += 2
            count[char] = c
        if any(count.values()):
            longest += 1
        return longest
# @lc code=end

print(Solution().longestPalindrome('abc'))

#
# @lcpr case=start
# "abccccdd"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#


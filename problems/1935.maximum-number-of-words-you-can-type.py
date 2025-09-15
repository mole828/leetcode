#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        brokenLetters = set(brokenLetters)
        res = 0
        for word in words:
            if not set(word) & brokenLetters:
                res += 1
        return res
# @lc code=end


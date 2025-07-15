#
# @lc app=leetcode id=3136 lang=python3
#
# [3136] Valid Word
#

# @lc code=start
import string


vowels = set('aeiouAEIOU')
allow_chars = set(string.digits+string.ascii_lowercase+string.ascii_uppercase)
class Solution:
    def isValid(self, word: str) -> bool:
        return all([
            len(word) >= 3,
            any(c in vowels for c in word),
            any((c not in string.digits and c not in vowels) for c in word),
            all(c in allow_chars for c in word),
        ])
# @lc code=end


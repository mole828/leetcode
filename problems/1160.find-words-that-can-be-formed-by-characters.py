#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCounter = Counter(chars)
        output = 0
        for word in words:
            wordCounter = Counter(word)
            # print(wordSet, wordSet < charsSet, charsSet)
            if wordCounter < charsCounter:
                output += len(word)
        return output
# @lc code=end

print(Solution().countCharacters(
    words=["cat","bt","hat","tree"],
    chars="atach"
))

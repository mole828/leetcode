#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        charSet1 = set(word1)
        charSet2 = set(word2)
        if charSet1 != charSet2:
            return False
        charCount1 = Counter(word1)
        charCount2 = Counter(word2) 
        print(charCount1,charCount2)
        countCount1 = Counter(charCount1[key] for key in charCount1)
        countCount2 = Counter(charCount2[key] for key in charCount2)
        print(countCount1, countCount2, countCount1==countCount2)
        return countCount1==countCount2
# @lc code=end

print(Solution().closeStrings(word1 = "cabbba", word2 = "abbccc"))
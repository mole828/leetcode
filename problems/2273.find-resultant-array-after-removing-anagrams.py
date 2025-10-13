#
# @lc app=leetcode id=2273 lang=python3
#
# [2273] Find Resultant Array After Removing Anagrams
#

# @lc code=start
from collections import Counter
from typing import List, Set


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        last_hash = None
        res = []
        for word in words:
            key = tuple(sorted(Counter(word).items()))
            print(word, key)
            if key != last_hash:
                last_hash = key
                res.append(word)
        return res
        
# @lc code=end

print(Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"]))  # ["bbaa","cd"]
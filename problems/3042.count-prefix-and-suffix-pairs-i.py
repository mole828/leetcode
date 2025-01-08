#
# @lc app=leetcode id=3042 lang=python3
# @lcpr version=
#
# [3042] Count Prefix and Suffix Pairs I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix_and_suffix(word1: str, word2:str):
            if len(word1) > len(word2):
                return False
            return word2.startswith(word1) and word2.endswith(word1)
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_prefix_and_suffix(words[i], words[j]):
                    count += 1
        return count
        
# @lc code=end



#
# @lcpr case=start
# ["a","aba","ababa","aa"]\n
# @lcpr case=end

# @lcpr case=start
# ["pa","papa","ma","mama"]\n
# @lcpr case=end

# @lcpr case=start
# ["abab","ab"]\n
# @lcpr case=end

#


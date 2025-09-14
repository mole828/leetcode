#
# @lc app=leetcode id=966 lang=python3
# @lcpr version=30204
#
# [966] Vowel Spellchecker
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def normalize(word: str) -> str:
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())
        wordlist_lower: dict[str, list[str]] = defaultdict(list)
        for w in wordlist:
            wordlist_lower[w.lower()].append(w)
        wordlist_normalize: dict[str, list[str]] = defaultdict(list)
        for w in wordlist:
            wordlist_normalize[normalize(w)].append(w)
        wordlist_set: set[str] = set(wordlist)
        res = []
        for q in queries:
            if q in wordlist_set:
                res.append(q)
            elif q.lower() in wordlist_lower:
                res.append(wordlist_lower[q.lower()][0])
            elif normalize(q) in wordlist_normalize:
                res.append(wordlist_normalize[normalize(q)][0])
            else:
                res.append('')
        return res
        
# @lc code=end

Solution().spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])

#
# @lcpr case=start
# ["KiTe","kite","hare","Hare"]\n["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]\n
# @lcpr case=end

# @lcpr case=start
# ["yellow"]\n["YellOw"]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=140 lang=python3
# @lcpr version=
#
# [140] Word Break II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        notes: List[str] = []
        def find_words(i: int, words: List[str]):
            if i == len(s):
                notes.append(' '.join(words))
                return
            last = s[i:]
            for word in wordDict:
                if last.find(word) == 0:
                    find_words(i+len(word), words+[word])
        find_words(0,[])
        return notes
# @lc code=end

print(Solution().wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))

#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#


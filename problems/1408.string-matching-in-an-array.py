#
# @lc app=leetcode id=1408 lang=python3
# @lcpr version=
#
# [1408] String Matching in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        ans = []
        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                if word in words[j]:
                    ans.append(word)
                    break
        return ans
        
# @lc code=end



#
# @lcpr case=start
# ["mass","as","hero","superhero"]\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode","et","code"]\n
# @lcpr case=end

# @lcpr case=start
# ["blue","green","bu"]\n
# @lcpr case=end

#


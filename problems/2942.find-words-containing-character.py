#
# @lc app=leetcode id=2942 lang=python3
# @lcpr version=30204
#
# [2942] Find Words Containing Character
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
        
# @lc code=end



#
# @lcpr case=start
# ["leet","code"]\n"e"\n
# @lcpr case=end

# @lcpr case=start
# ["abc","bcd","aaaa","cbc"]\n"a"\n
# @lcpr case=end

# @lcpr case=start
# ["abc","bcd","aaaa","cbc"]\n"z"\n
# @lcpr case=end

#


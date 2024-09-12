#
# @lc app=leetcode id=1684 lang=python3
# @lcpr version=
#
# [1684] Count the Number of Consistent Strings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum( 0 if set(word) - allowed else 1 for word in words )
        
# @lc code=end



#
# @lcpr case=start
# "ab"\n["ad","bd","aaab","baa","badab"]\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n["a","b","c","ab","ac","bc","abc"]\n
# @lcpr case=end

# @lcpr case=start
# "cad"\n["cc","acd","b","ba","bac","bad","ac","d"]\n
# @lcpr case=end

#


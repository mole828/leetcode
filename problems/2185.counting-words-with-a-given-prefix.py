#
# @lc app=leetcode id=2185 lang=python3
# @lcpr version=
#
# [2185] Counting Words With a Given Prefix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count
        
# @lc code=end



#
# @lcpr case=start
# ["pay","attention","practice","attend"]\n"at"\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode","win","loops","success"]\n"code"\n
# @lcpr case=end

#


#
# @lc app=leetcode id=344 lang=python3
# @lcpr version=
#
# [344] Reverse String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        c = s.copy()
        c.reverse()
        for i in range(len(s)):
            s[i] = c[i]
        
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#


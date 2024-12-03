#
# @lc app=leetcode id=2109 lang=python3
# @lcpr version=
#
# [2109] Adding Spaces to a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces_set = set(spaces)
        return ''.join((' ' if i in spaces_set else '')+c for i,c in enumerate(s))
# @lc code=end



#
# @lcpr case=start
# "LeetcodeHelpsMeLearn"\n[8,13,15]\n
# @lcpr case=end

# @lcpr case=start
# "icodeinpython"\n[1,5,7,9]\n
# @lcpr case=end

# @lcpr case=start
# "spacing"\n[0,1,2,3,4,5,6]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=2191 lang=python3
# @lcpr version=
#
# [2191] Sort the Jumbled Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def trans(x: int):
            return int(''.join(str(mapping[int(c)]) for c in str(x)))
        return sorted(nums, key=trans)
# @lc code=end

print(Solution().sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))

#
# @lcpr case=start
# [8,9,4,0,2,1,3,5,7,6]\n[991,338,38]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,4,5,6,7,8,9]\n[789,456,123]\n
# @lcpr case=end

#


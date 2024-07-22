#
# @lc app=leetcode id=2418 lang=python3
# @lcpr version=
#
# [2418] Sort the People
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _,name in sorted(zip(heights,names),reverse=True)]
# @lc code=end



#
# @lcpr case=start
# ["Mary","John","Emma"]\n[180,165,170]\n
# @lcpr case=end

# @lcpr case=start
# ["Alice","Bob","Bob"]\n[155,185,150]\n
# @lcpr case=end

#


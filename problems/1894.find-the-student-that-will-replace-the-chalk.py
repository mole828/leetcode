#
# @lc app=leetcode id=1894 lang=python3
# @lcpr version=
#
# [1894] Find the Student that Will Replace the Chalk
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        k = k % total
        for i in range(n):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        return -1
# @lc code=end



#
# @lcpr case=start
# [5,1,5]\n22\n
# @lcpr case=end

# @lcpr case=start
# [3,4,1,2]\n25\n
# @lcpr case=end

#


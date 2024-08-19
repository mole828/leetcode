#
# @lc app=leetcode id=650 lang=python3
# @lcpr version=
#
# [650] 2 Keys Keyboard
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import numpy as np


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def dp(dx: int, has: int, step: int):
            if has == n:
                return step
            if has > n:
                return np.inf
            return min( dp(dx, has+dx, step+1), dp(has, has+has, step+2), )
        return dp(dx=1, has=1, step=1)

# @lc code=end

print(Solution().minSteps(3))

#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


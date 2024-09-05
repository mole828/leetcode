#
# @lc app=leetcode id=2028 lang=python3
# @lcpr version=
#
# [2028] Find Missing Observations
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        for roll in rolls:
            total -= roll
        if total < n or total > n * 6:
            return []
        res = [total // n] * n
        for i in range(total % n):
            res[i] += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [3,2,4,3]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,5,6]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n6\n4\n
# @lcpr case=end

#


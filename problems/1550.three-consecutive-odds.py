#
# @lc app=leetcode id=1550 lang=python3
# @lcpr version=
#
# [1550] Three Consecutive Odds
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# day2 2025-05-11
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        last = 3
        for x in arr:
            if x % 2 == 0:
                last = 3
            else:
                last -= 1
                if not last:
                    return True
        return False
# @lc code=end



#
# @lcpr case=start
# [2,6,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,34,3,4,5,7,23,12]\n
# @lcpr case=end

#


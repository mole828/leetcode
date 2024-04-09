#
# @lc app=leetcode id=2073 lang=python3
# @lcpr version=
#
# [2073] Time Needed to Buy Tickets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0 
        t = 0 
        while tickets[k]: 
            if tickets[i]: 
                tickets[i] -= 1 
                t += 1
            i += 1
            if i==len(tickets):
                i = 0
        return t 
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#


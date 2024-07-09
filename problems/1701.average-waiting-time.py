#
# @lc app=leetcode id=1701 lang=python3
# @lcpr version=
#
# [1701] Average Waiting Time
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cus = customers.copy()
        last_end = 0
        waits = []
        while cus:
            arrives, take = cus.pop(0)
            this_end = max(last_end, arrives) + take
            wait =  this_end - arrives
            last_end = this_end
            waits.append(wait)
        return sum(waits)/len(waits)
            
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,5],[4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,2],[5,4],[10,3],[20,1]]\n
# @lcpr case=end

#


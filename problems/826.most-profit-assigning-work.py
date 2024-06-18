#
# @lc app=leetcode id=826 lang=python3
# @lcpr version=
#
# [826] Most Profit Assigning Work
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from bisect import bisect_left

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_and_profit = sorted(zip(difficulty, profit))
        _high_prof = 0
        for i in range(len(difficulty_and_profit)):
            d,_prof = difficulty_and_profit[i]
            if _high_prof > _prof:
                difficulty_and_profit[i] = (d,_high_prof)
            _high_prof = max(_prof, _high_prof)
        print(difficulty_and_profit)
        worker_profit_max = [0]*len(worker)
        
        for i in range(len(worker)):
            worker_diff = worker[i]
            j = bisect_left(difficulty_and_profit, (worker_diff,999999))
            if j:
                d,p = difficulty_and_profit[j-1]
                worker_profit_max[i] = p
        print(worker_profit_max)
        return sum(worker_profit_max)
# @lc code=end

print(Solution().maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
print(Solution().maxProfitAssignment([85,47,57],[24,66,99],[40,25,25]))

#
# @lcpr case=start
# [2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [85,47,57]\n[24,66,99]\n[40,25,25]\n
# @lcpr case=end

#


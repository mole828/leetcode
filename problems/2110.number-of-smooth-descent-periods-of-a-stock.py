#
# @lc app=leetcode id=2110 lang=python3
# @lcpr version=30204
#
# [2110] Number of Smooth Descent Periods of a Stock
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        last_num = prices[0]
        window = 1
        ans = 0
        for i in range(1, n):
            num = prices[i]
            if last_num - num == 1:
                window += 1
            else:
                ans += (window + 1) * window // 2
                # print(i, window, ans)
                window = 1
            last_num = num
        if window > 0:
            ans += (window + 1) * window // 2
        return ans
# @lc code=end

print(Solution().getDescentPeriods([3,2,1,4]))

#
# @lcpr case=start
# [3,2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [8,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


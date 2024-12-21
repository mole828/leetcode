#
# @lc app=leetcode id=1475 lang=python3
# @lcpr version=
#
# [1475] Final Prices With a Special Discount in a Shop
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if not stack:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - stack[-1]
            stack.append(prices[i])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [8,4,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,1,6]\n
# @lcpr case=end

#


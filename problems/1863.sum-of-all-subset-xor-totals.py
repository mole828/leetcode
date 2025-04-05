#
# @lc app=leetcode id=1863 lang=python3
# @lcpr version=
#
# [1863] Sum of All Subset XOR Totals
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# day1 May 20, 2024
# day2 April 5, 2025
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.sum = 0
        def dp(i: int, sub: int):
            if i == len(nums):
                self.sum += sub
                return
            now = nums[i]
            dp(i+1, sub)
            dp(i+1, sub^now)
        dp(0,0)
        return self.sum
        
# @lc code=end



#
# @lcpr case=start
# [1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,6,7,8]\n
# @lcpr case=end

#


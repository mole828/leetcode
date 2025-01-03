#
# @lc app=leetcode id=2270 lang=python3
# @lcpr version=
#
# [2270] Number of Ways to Split Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        first_sum = 0
        second_sum = sum(nums)
        ans = 0
        for num in nums[:-1]:
            first_sum += num
            second_sum -= num
            print(first_sum, second_sum)
            if first_sum >= second_sum:
                ans += 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [10,4,-8,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,0]\n
# @lcpr case=end

#


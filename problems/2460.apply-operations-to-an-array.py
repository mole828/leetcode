#
# @lc app=leetcode id=2460 lang=python3
# @lcpr version=30204
#
# [2460] Apply Operations to an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = 2 * nums[i-1]
                nums[i] = 0
        ans = [num for num in nums if num != 0]
        ans += [0] * (len(nums) - len(ans))
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#


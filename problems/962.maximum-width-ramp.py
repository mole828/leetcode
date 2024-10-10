#
# @lc app=leetcode id=962 lang=python3
# @lcpr version=
#
# [962] Maximum Width Ramp
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        result = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                result = max(result, i - stack.pop())

        return result
# @lc code=end



#
# @lcpr case=start
# [6,0,8,2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [9,8,1,0,1,9,4,0,4,1]\n
# @lcpr case=end

#


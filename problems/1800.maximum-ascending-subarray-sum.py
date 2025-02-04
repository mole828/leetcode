#
# @lc app=leetcode id=1800 lang=python3
# @lcpr version=30204
#
# [1800] Maximum Ascending Subarray Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        left, right = 0, 0
        while right < len(nums):
            while right < len(nums) and (right == 0 or nums[right] > nums[right-1]):
                right += 1
            max_sum = max(max_sum, sum(nums[left:right]))
            left = right
            right += 1
        return max_sum
        
# @lc code=end

print(Solution().maxAscendingSum([10,20,30,5,10,50]))  # 65

#
# @lcpr case=start
# [10,20,30,5,10,50]\n
# @lcpr case=end

# @lcpr case=start
# [10,20,30,40,50]\n
# @lcpr case=end

# @lcpr case=start
# [12,17,15,13,10,11,12]\n
# @lcpr case=end

#


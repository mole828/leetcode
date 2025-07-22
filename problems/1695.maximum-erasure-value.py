#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        sum_of_window = 0
        set_of_window = set()
        while right < len(nums):
            right_value = nums[right]
            while right_value in set_of_window:
                left_value = nums[left]
                set_of_window.remove(left_value)
                sum_of_window -= left_value
                left += 1
            set_of_window.add(right_value)
            sum_of_window += right_value
            ans = max(ans, sum_of_window)
            right += 1
        return ans

# @lc code=end

print(Solution().maximumUniqueSubarray([4,2,4,5,6]))

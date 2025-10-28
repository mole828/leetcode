#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#

# @lc code=start
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sum_of_nums = sum(nums)
        n = len(nums)
        left = 0
        right = sum_of_nums
        ans = 0
        for i in range(n):
            num = nums[i]
            left += num
            right -= num
            if not num:
                d = right - left
                match d:
                    case 0:
                        ans += 2
                    case 1 | -1:
                        ans += 1
        return ans
        
# @lc code=end


#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(
            num - sum(int(c) for c in str(num)) for num in nums
        )
        
# @lc code=end


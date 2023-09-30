#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from collections import Counter
from typing import List

from sortedcontainers import SortedList


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, third = [], float('-inf')
        
        for num in reversed(nums):
            # print(stack, third)
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
        

# @lc code=end
print(Solution().find132pattern([1,2,3,4]))
print(Solution().find132pattern([3,1,4,2]))
print(Solution().find132pattern([2,1,3]))

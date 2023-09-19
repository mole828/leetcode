#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num 
            s.add(num)
        
# @lc code=end


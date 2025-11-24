#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        cur = 0
        for num in nums:
            cur = (cur << 1 | num) 
            ans.append(cur % 5 == 0)
        return ans

# @lc code=end


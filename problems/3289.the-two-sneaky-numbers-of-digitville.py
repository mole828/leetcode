#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        has = set()
        for v in nums:
            if v in has:
                ans.append(v)
            else:
                has.add(v)
        return ans
# @lc code=end


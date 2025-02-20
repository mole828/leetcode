#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums_set = set(nums)
        def dfs(last: int):
            if last == 0:
                yield ''
                return
            for i in range(2):
                for last_str in dfs(last - 1):
                    yield str(i) + last_str
        for possible in dfs(n):
            if possible not in nums_set:
                return possible
        return ''
        
        
# @lc code=end


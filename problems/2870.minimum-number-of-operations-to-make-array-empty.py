#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        output = 0
        for key in counter:
            last = counter[key]
            if last == 1:
                return -1
            mod = last % 3
            if mod:
                output += 1  
            output += last//3
        return output
# @lc code=end


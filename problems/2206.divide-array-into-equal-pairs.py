#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for k,v in counter.items():
            if v % 2 != 0:
                return False
        return True
        
# @lc code=end


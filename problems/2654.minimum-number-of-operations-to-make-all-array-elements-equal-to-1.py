#
# @lc app=leetcode id=2654 lang=python3
#
# [2654] Minimum Number of Operations to Make All Array Elements Equal to 1
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1
        min_size = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_size = min(min_size, j - i)
                    break
        return min_size + n - 1
        
# @lc code=end


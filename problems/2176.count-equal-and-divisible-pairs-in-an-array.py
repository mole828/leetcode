#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if a == b and (i*j)%k == 0:
                    count += 1
        return count

        
# @lc code=end


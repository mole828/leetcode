#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = sum(candies) // k + 1
        def check(x):
            total = 0
            for candie in candies:
                total += candie//x
            return total >= k
        while left+1 < right :
            mid = (left+right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
        
# @lc code=end


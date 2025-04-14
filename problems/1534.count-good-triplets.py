#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good(x, y, z):
            return all([
                abs(x-y) <= a,
                abs(y-z) <= b,
                abs(z-x) <= c,
            ])
        
        return sum(
            is_good(x, y, z) 
            for i, x in enumerate(arr) 
            for j, y in enumerate(arr[i+1:]) 
            for k, z in enumerate(arr[i+j+2:])
        )
        
# @lc code=end

print(Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
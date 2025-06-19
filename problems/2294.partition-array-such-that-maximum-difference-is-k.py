#
# @lc app=leetcode id=2294 lang=python3
#
# [2294] Partition Array Such That Maximum Difference Is K
#

# @lc code=start
from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        mn = - float('inf')
        for x in nums:
            if x - mn > k:
                ans += 1
                mn = x  
        return ans
        
# @lc code=end


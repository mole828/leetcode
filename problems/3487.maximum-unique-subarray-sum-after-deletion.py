#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        temp = [-num for num in nums]
        heapq.heapify(temp)
        result_set = set()
        result_set.add(-heapq.heappop(temp))
        while temp:
            num = -heapq.heappop(temp)
            if num < 0:
                break
            result_set.add(num)
            
        return sum(result_set)
        
# @lc code=end


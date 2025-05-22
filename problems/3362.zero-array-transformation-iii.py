#
# @lc app=leetcode id=3362 lang=python3
#
# [3362] Zero Array Transformation III
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        diff = [0] * (len(nums) + 1)
        que: List[int] = []
        sum_d = j = 0 
        for i, x in enumerate(nums):
            sum_d += diff[i]
            while j < len(queries) and queries[j][0] <= i:
                heapq.heappush(que, -queries[j][1])
                j += 1
            while sum_d < x and que and -que[0] >= i:
                sum_d += 1
                diff[-heapq.heappop(que) + 1] -= 1
            if sum_d < x:
                return -1 
        return len(que)
        
# @lc code=end


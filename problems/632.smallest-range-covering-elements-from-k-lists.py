#
# @lc app=leetcode id=632 lang=python3
# @lcpr version=
#
# [632] Smallest Range Covering Elements from K Lists
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq

        heap = []
        max_value = float("-inf")
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num[0], i, 0))
            max_value = max(max_value, num[0])

        result = [heap[0][0], max_value]
        while heap:
            min_value, i, j = heapq.heappop(heap)
            if max_value - min_value < result[1] - result[0]:
                result = [min_value, max_value]

            if j + 1 < len(nums[i]):
                heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
                max_value = max(max_value, nums[i][j + 1])
            else:
                break

        return result
        
# @lc code=end



#
# @lcpr case=start
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#


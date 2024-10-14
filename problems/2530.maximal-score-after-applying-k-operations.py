#
# @lc app=leetcode id=2530 lang=python3
# @lcpr version=
#
# [2530] Maximal Score After Applying K Operations
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        result = 0
        for _ in range(k):
            max_value = -heapq.heappop(heap)
            result += max_value
            heapq.heappush(heap, -math.ceil(max_value / 3))

        return result
# @lc code=end



#
# @lcpr case=start
# [10,10,10,10,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,3,3]\n3\n
# @lcpr case=end

#


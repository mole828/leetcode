#
# @lc app=leetcode id=3066 lang=python3
# @lcpr version=30204
#
# [3066] Minimum Operations to Exceed Threshold Value II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations_count = 0
        while nums:
            a = heapq.heappop(nums)
            if a >= k:
                return operations_count
            b = heapq.heappop(nums)
            new_val = a*2+b
            heapq.heappush(nums, new_val)
            operations_count += 1
        return -1

        
# @lc code=end



#
# @lcpr case=start
# [2,11,10,1,3]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,4,9]\n20\n
# @lcpr case=end

#


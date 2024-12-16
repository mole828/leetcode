#
# @lc app=leetcode id=3264 lang=python3
# @lcpr version=
#
# [3264] Final Array State After K Multiplication Operations I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            num, idx = heapq.heappop(heap)
            nums[idx] *= multiplier
            heapq.heappush(heap, (num * multiplier, idx))
            k -= 1
        return nums
        
# @lc code=end

print(Solution().getFinalState([2,1,3,5,6], 5, 2))

#
# @lcpr case=start
# [2,1,3,5,6]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n3\n4\n
# @lcpr case=end

#


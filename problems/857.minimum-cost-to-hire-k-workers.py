#
# @lc app=leetcode id=857 lang=python3
# @lcpr version=
#
# [857] Minimum Cost to Hire K Workers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        total_wage, total_quality, max_heap = float('inf'), 0, []
        for ratio, q in sorted([(w/q, q) for w, q in zip(wage, quality)]):
            total_quality += q
            heappush(max_heap, -q)
            if len(max_heap) == k:
                # print(max_heap, total_wage, total_quality)
                total_wage = min(total_wage, total_quality * ratio)
                # total_wage = min(total_wage, -sum(max_heap) * ratio)
                # heappop(max_heap)
                total_quality += heappop(max_heap)
            # print(max_heap, total_wage, total_quality)
        return total_wage
# @lc code=end

print(Solution().mincostToHireWorkers([10,20,5], [70,50,30], 2))
print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))

#
# @lcpr case=start
# [10,20,5]\n[70,50,30]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,1,10,10,1]\n[4,8,2,2,7]\n3\n
# @lcpr case=end

#


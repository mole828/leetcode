#
# @lc app=leetcode id=2594 lang=python3
# @lcpr version=30204
#
# [2594] Minimum Time to Repair Cars
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def fixCost(self, rank: int, cars: int):
        return rank * (cars**2)

    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        heap: tuple[int, int, int] = [] # nextCost, index, rank, needFix
        heapq.heapify(heap)
        for i in range(n):
            rank = ranks[i]
            nextCost = self.fixCost(rank, 1)
            heapq.heappush(heap, (nextCost, i, rank, 0,))

        # print(heap)
        while cars:
            nextCost, index, rank, needFix = heapq.heappop(heap)
            newNextCost = self.fixCost(rank, needFix+2)
            heapq.heappush(heap, (newNextCost, index, rank, needFix+1))
            cars -= 1
            # print(f"{index}: {rank}, cost: {nextCost}")
            
        # print(heap)
        
        return max(self.fixCost(rank, needFix) for _,_,rank,needFix in heap)

        
# @lc code=end

print(Solution().repairCars(ranks=[4,2,3,1], cars=10))

#
# @lcpr case=start
# [4,2,3,1]\n10\n
# @lcpr case=end

# @lcpr case=start
# [5,1,8]\n6\n
# @lcpr case=end

#


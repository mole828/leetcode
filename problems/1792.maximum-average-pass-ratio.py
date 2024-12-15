#
# @lc app=leetcode id=1792 lang=python3
# @lcpr version=30204
#
# [1792] Maximum Average Pass Ratio
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        delta_heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapq.heapify(delta_heap)
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(delta_heap)
            p += 1
            t += 1
            heapq.heappush(delta_heap, (p / t - (p + 1) / (t + 1), p, t))

        return sum(p / t for _, p, t in delta_heap) / len(classes)
        
# @lc code=end



#
# @lcpr case=start
# [[1,2],[3,5],[2,2]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,9],[4,5],[2,10]]\n4\n
# @lcpr case=end

#


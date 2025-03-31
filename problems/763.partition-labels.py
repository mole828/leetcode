#
# @lc app=leetcode id=763 lang=python3
# @lcpr version=30204
#
# [763] Partition Labels
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        heap = []
        heapq.heapify(heap)
        for i in first:
            left = first[i]
            right = last[i]
            heapq.heappush(heap, (left, 0))
            heapq.heappush(heap, (right, 1))
        in_part = 0
        last_index = 0
        parts = []
        while heap:
            index, io = heapq.heappop(heap)
            if io == 0:
                in_part += 1
            else:
                in_part -= 1
            if not in_part:
                parts.append(index - last_index + 1)
                last_index = index + 1
        return parts

# @lc code=end

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

#
# @lcpr case=start
# "ababcbacadefegdehijhklij"\n
# @lcpr case=end

# @lcpr case=start
# "eccbbbbdec"\n
# @lcpr case=end

#


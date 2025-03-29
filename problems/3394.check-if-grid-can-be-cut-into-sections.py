#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
from enum import Enum
import heapq
from typing import List


class Solution:
    class Status(Enum):
        BEGIN = 1
        END = 0
        def __lt__(self, other: 'Solution.Status'):
            return self.value < other.value
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y_heap = []
        x_heap = []
        for start_x, start_y, end_x, end_y in rectangles:
            heapq.heappush(y_heap, (start_y, self.Status.BEGIN))
            heapq.heappush(y_heap, (end_y, self.Status.END))
            heapq.heappush(x_heap, (start_x, self.Status.BEGIN))
            heapq.heappush(x_heap, (end_x, self.Status.END))

        def find(heap):
            inline = 0
            inline_zero_count = 0
            while heap:
                i, status = heapq.heappop(heap)
                if status == self.Status.BEGIN:
                    inline += 1
                elif status == self.Status.END:
                    inline -= 1
                if inline == 0:
                    inline_zero_count += 1
            return inline_zero_count
        
        y_count = find(y_heap)
        x_count = find(x_heap)
        return y_count >= 3 or x_count >= 3

# @lc code=end

print(Solution().checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
from enum import Enum
import heapq
from typing import List


class Solution:
    class MeetingStatus(Enum):
        BEGIN = 0
        END = 1
        def __lt__(self, other: 'Solution.MeetingStatus'):
            return self.value < other.value

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        heap = []
        for a, b in meetings:
            heapq.heappush(heap, (a, self.MeetingStatus.BEGIN))
            heapq.heappush(heap, (b, self.MeetingStatus.END))

        last = 1
        deep = 0
        result = 0
        while heap:
            i, status = heapq.heappop(heap)
            match status:
                case self.MeetingStatus.BEGIN:
                    if deep == 0:
                        result += i - last
                    deep += 1
                case self.MeetingStatus.END:
                    deep -= 1
                    if deep == 0:
                        last = i + 1
        result += days - last + 1
        return result

# @lc code=end

print(Solution().countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(Solution().countDays(days = 8, meetings = [[3,4],[4,8],[2,5],[3,8]]))
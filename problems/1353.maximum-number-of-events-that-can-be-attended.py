#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#

# @lc code=start
import heapq
from typing import List

# Wrong Answer
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        days: set[int] = set()
        heap = [
            (b-a, a, b)
            for a,b in events
        ]
        heapq.heapify(heap)
        while heap:
            _, a, b = heapq.heappop(heap)
            # print()
            for day in range(a, b + 1):
                if day not in days:
                    days.add(day)
                    break
        return len(days)
    
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        mx = max(e[1] for e in events) 

        groups = [[] for _ in range(mx + 1)]
        for e in events:
            groups[e[0]].append(e[1])

        ans = 0
        h = []
        for i, g in enumerate(groups):
            while h and h[0] < i:
                heapq.heappop(h)
            for end_day in g:
                heapq.heappush(h, end_day)
            if h:
                ans += 1
                heapq.heappop(h)
        return ans


# @lc code=end

print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]))
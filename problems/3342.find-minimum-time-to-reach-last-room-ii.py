#
# @lc app=leetcode id=3342 lang=python3
#
# [3342] Find Minimum Time to Reach Last Room II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        has: set[tuple[int, int]] = set()
        que = [(0,0,0,2)] # t, x, y, d
        heapq.heapify(que)
        while que:
            t, x, y, d = heapq.heappop(que)
            if (x, y) in has:
                continue
            has.add((x, y))
            if x == n-1 and y == m-1:
                return t
            next_d = 1 if d == 2 else 2
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    heapq.heappush(que, (max(t + next_d,  moveTime[nx][ny] + next_d), nx, ny, next_d))
            
            
        
# @lc code=end

print(Solution().minTimeToReach([[0,4],[4,4]]))
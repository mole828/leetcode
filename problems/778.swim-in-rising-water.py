#
# @lc app=leetcode id=778 lang=python3
# @lcpr version=30204
#
# [778] Swim in Rising Water
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = [(grid[0][0], 0, 0)]  # (time, x, y)
        visited = set()
        while que:
            time, x, y = heapq.heappop(que)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if x == n - 1 and y == n - 1:
                return time
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(que, (max(time, grid[nx][ny]), nx, ny))
        
# @lc code=end



#
# @lcpr case=start
# [[0,2],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1368 lang=python3
# @lcpr version=30204
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    D_MAP = [None, (0, 1), (0, -1), (1, 0), (-1, 0)]
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        visited: map[tuple[int, int], int] = {}
        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited[(x, y)] = cost
            if x == m - 1 and y == n - 1:
                return cost
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_cost = cost + (0 if Solution.D_MAP[grid[x][y]] == d else 1)
                dx, dy = d
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    heapq.heappush(heap, (new_cost, nx, ny))
        return 10000
        
# @lc code=end


print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))  # 3

#
# @lcpr case=start
# [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,3],[3,2,2],[1,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[4,3]]\n
# @lcpr case=end

#


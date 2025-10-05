#
# @lc app=leetcode id=417 lang=python3
# @lcpr version=30204
#
# [417] Pacific Atlantic Water Flow
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for c in range(cols):
            pacific_reachable.add((0, c))
            atlantic_reachable.add((rows - 1, c))
        for r in range(rows):
            pacific_reachable.add((r, 0))
            atlantic_reachable.add((r, cols - 1))
        def bfs(reachable: set[tuple[int, int]]):
            queue = deque(reachable)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                        reachable.add((nr, nc))
                        queue.append((nr, nc))
        bfs(pacific_reachable)
        bfs(atlantic_reachable)
        return list(pacific_reachable & atlantic_reachable)
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#


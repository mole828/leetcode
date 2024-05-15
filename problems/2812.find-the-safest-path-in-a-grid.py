#
# @lc app=leetcode id=2812 lang=python3
# @lcpr version=
#
# [2812] Find the Safest Path in a Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
import heapq
from typing import List

import numpy as np


class Solution:
    # Wrong Answer, 1028/1036 cases passed (N/A)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        matrix = np.copy(grid)
        rows, cols = matrix.shape
        print(matrix)

        dist_matrix = np.full((len(grid),len(grid[0])), np.inf)
        # print(dist_matrix)
        def diffusion(y: int, x: int):
            row_indices = np.arange(rows)[:,np.newaxis]
            col_indices = np.arange(cols)
            manhattan_distance = np.abs(row_indices-y)+np.abs(col_indices-x)
            nonlocal dist_matrix
            # print(row_indices, col_indices, manhattan_distance)
            dist_matrix = np.minimum(dist_matrix,manhattan_distance)
        for y,x in list(zip(*matrix.nonzero())):
            diffusion(y,x)
        print(dist_matrix)

        def next_step(y: int, x: int):
            ty = y+1
            if ty < rows:
                yield (ty, x)
            tx = x+1
            if tx < cols:
                yield (y, tx)
        @cache
        def dp(y: int = 0, x: int = 0) -> int:
            this = dist_matrix[y,x]
            if not this:
                return 0
            return max([min(this, dp(yy,xx)) for yy,xx in next_step(y,x)],default=this)
        return int(dp())

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # 不做这一判断就无法通过最后一题
        # 不知道算是用例不合理，还是算法不过关
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]: 
            return 0
        
        matrix = np.copy(grid)
        rows, cols = matrix.shape
        print(matrix)

        dist_matrix = np.full((len(grid),len(grid[0])), np.inf)
        # print(dist_matrix)
        def diffusion(y: int, x: int):
            row_indices = np.arange(rows)[:,np.newaxis]
            col_indices = np.arange(cols)
            manhattan_distance = np.abs(row_indices-y)+np.abs(col_indices-x)
            nonlocal dist_matrix
            # print(row_indices, col_indices, manhattan_distance)
            dist_matrix = np.minimum(dist_matrix,manhattan_distance)
        for y,x in list(zip(*matrix.nonzero())):
            diffusion(y,x)

        pq = [(-dist_matrix[0,0], 0,0)]
        heapq.heapify(pq)

        has_add = set()
        def add_step(y: int, x: int, safe):
            yx = (y,x)
            if yx in has_add:
                return
            has_add.add(yx)
            if 0<=y<rows and 0<=x<cols:
                min_safe = min(safe, dist_matrix[y,x])
                heapq.heappush(pq, (-min_safe,y,x))

        while pq:
            nsafe, y, x = heapq.heappop(pq)
            safe = -nsafe
            if x == cols - 1 and y == rows - 1:
                return int(safe)
            for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_y = y + dy
                new_x = x + dx
                add_step(new_y, new_x, safe)
            

# @lc code=end

# print(Solution().maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
print(Solution().maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))
print(Solution().maximumSafenessFactor([[0,1,1],[0,1,1],[0,1,1]]))

#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1],[0,0,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1976 lang=python3
# @lcpr version=30204
#
# [1976] Number of Ways to Arrive at Destination
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import functools
from typing import List

import numpy


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # 初始化邻接矩阵
        mat = numpy.full((n, n), numpy.inf)
        numpy.fill_diagonal(mat, 0)

        # 填充直接相连的边
        for i, j, w in roads:
            mat[i][j] = w
            mat[j][i] = w

        normal = mat.copy()

        # Floyd-Warshall算法更新最短路径
        for k in range(n):
            mat = numpy.minimum(mat, mat[:, k, None] + mat[k, :])

        target_cost = mat[0][-1]
        target_node = n - 1

        # 寻找和最短路径等长的路径
        @functools.cache
        def dfs(node: int) -> int:
            if node == target_node:
                return 1
            count = 0
            for next_node, cost in enumerate(normal[node]):
                if next_node == node:
                    continue
                if mat[next_node][target_node] + cost == mat[node][target_node]:
                    count += dfs(next_node)
            return count
        
        return dfs(0) % (10 ** 9 + 7)

# @lc code=end

print(Solution().countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))  # 4

#
# @lcpr case=start
# 7\n[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0,10]]\n
# @lcpr case=end

#


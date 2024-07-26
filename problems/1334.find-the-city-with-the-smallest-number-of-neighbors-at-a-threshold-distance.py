#
# @lc app=leetcode id=1334 lang=python3
# @lcpr version=
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import numpy as np

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = np.full((n,n), np.inf)
        for i in range(n):
            mat[i][i] = 0
        for a,b,c in edges:
            mat[a][b] = c
            mat[b][a] = c

        for k in range(n):
            mat = np.minimum(mat, mat[:,k,None] + mat[None,k,:])

        counts = np.sum(mat > distanceThreshold, axis=1)
        max_count = np.max(counts)
        max_indices = np.argwhere(counts == max_count)
        max_index = np.max(max_indices)

        return max_index
        
# @lc code=end

print(Solution().findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))

#
# @lcpr case=start
# 4\n[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]\n2\n
# @lcpr case=end

#


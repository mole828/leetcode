#
# @lc app=leetcode id=834 lang=python3
# @lcpr version=
#
# [834] Sum of Distances in Tree
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np


class Solution:
    # Memory Limit Exceeded, 64/74 cases passed (N/A)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        mat = np.full((n,n), np.inf)
        np.fill_diagonal(mat, 0)
        for a,b in edges:
            mat[a,b] = 1
            mat[b,a] = 1
        for k in range(n):
            mat = np.minimum(mat, mat[:,k, None] + mat[None, k, :]) 
        return [np.sum(row, dtype=int) for row in mat]
    
    # Time Limit Exceeded, 64/74 cases passed (N/A)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        mat = [[np.inf]*n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 0
        for a,b in edges:
            mat[a][b] = 1
            mat[b][a] = 1
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    mat[j][k] = min(mat[j][k], mat[i][j]+mat[i][k])
        return [sum(row) for row in mat]
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        link = [set() for _ in range(n)]
        for a,b in edges:
            link[a].add(b)
            link[b].add(a)
        count = [1] * n  
        ans = [0] * n  
        
        def dfs(node: int = 0, parent: int = None):
            for child in link[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node: int = 0, parent: int = None):
            for child in link[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
        
# @lc code=end

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))

#
# @lcpr case=start
# 6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=310 lang=python3
# @lcpr version=
#
# [310] Minimum Height Trees
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import numpy

class Solution:
    # Time Limit Exceeded, 58 / 71 testcases passed
    def findMinHeightTrees(self, n: int, edges: List[tuple[int]]) -> List[int]:
        matrix = numpy.full((n,n), numpy.inf)
        numpy.fill_diagonal(matrix, 0)
        for a,b in edges:
            matrix[a,b]=1
            matrix[b,a]=1
        for k in range(n):
            matrix = numpy.minimum(matrix, matrix[:, k, None] + matrix[None, k, :])
        rows_max = matrix.max(axis=1)
        min_deep = rows_max.min()
        # print(numpy.where(rows_max==min_deep))
        optimal_locations = numpy.where(rows_max == min_deep)[0]
        return optimal_locations
    
    def findMinHeightTrees(self, n: int, edges: List[tuple[int]]) -> List[int]:
        if n == 1: 
            return [0]
        adj:list[set[int]] = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            print(leaves)
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
        
# @lc code=end

print(Solution().findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))
print(Solution().findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(Solution().findMinHeightTrees(1,[]))

#
# @lcpr case=start
# 4\n[[1,0],[1,2],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[3,0],[3,1],[3,2],[3,4],[5,4]]\n
# @lcpr case=end

#


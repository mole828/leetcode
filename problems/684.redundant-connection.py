#
# @lc app=leetcode id=684 lang=python3
# @lcpr version=30204
#
# [684] Redundant Connection
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)

        for edge in edges:
            x, y = edge[0], edge[1]
            if find(x) == find(y):
                return [x, y]
            union(x, y)
        
        return []
    
# @lc code=end



#
# @lcpr case=start
# [[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,4],[1,5]]\n
# @lcpr case=end

#


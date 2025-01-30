#
# @lc app=leetcode id=2493 lang=python3
# @lcpr version=30204
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        color = [0] * (n+1)

        def dfs(u, fa, c):
            node.append(u)
            color[u] = c
            for v in g[u]:
                if v == fa: continue
                if color[v] == c or color[v] ==0 and not dfs(v, u, c ^ 3):
                    return False
            return True

        def bfs(u):
            q = deque([u])
            step = 0
            vis = set()
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u in vis: continue
                    vis.add(u)
                    for v in g[u]:
                        if v not in vis:
                            q.append(v)
                step += 1
            return step

        res = 0
        for i in range(1, n + 1):
            node = []
            if color[i] == 0:
                if not dfs(i, -1, 1):
                    return -1
                ans = 0
                for u in node:
                    ans = max(ans, bfs(u))
                res += ans

        return res
        
# @lc code=end



#
# @lcpr case=start
# 6\n[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[2,3],[3,1]]\n
# @lcpr case=end

#


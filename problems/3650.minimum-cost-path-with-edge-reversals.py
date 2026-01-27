#
# @lc app=leetcode id=3650 lang=python3
#
# [3650] Minimum Cost Path with Edge Reversals
#

# @lc code=start
from math import inf
from typing import List
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u,v, wt in edges:
            g[u].append((v, wt))
            g[v].append((u, wt * 2))
        dis = [inf] * n
        dis[0] = 0  
        que = [(0, 0)]
        while que:
            d, u = heapq.heappop(que)
            if d > dis[u]:
                continue
            for v, wt in g[u]:
                if dis[u] + wt < dis[v]:
                    dis[v] = dis[u] + wt
                    heapq.heappush(que, (dis[v], v))
        return dis[n - 1] if dis[n - 1] != inf else -1
# @lc code=end


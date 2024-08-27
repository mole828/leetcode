#
# @lc app=leetcode id=1514 lang=python3
# @lcpr version=
#
# [1514] Path with Maximum Probability
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        from collections import defaultdict
        from heapq import heappop, heappush

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        dist = [0] * n
        dist[start_node] = 1
        pq = [(-1, start_node)]
        while pq:
            d, u = heappop(pq)
            if u == end_node:
                return -d
            for v, w in graph[u]:
                if -d * w > dist[v]:
                    dist[v] = -d * w
                    heappush(pq, (-dist[v], v))
        return 0
        
# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.3]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[0.5]\n0\n2\n
# @lcpr case=end

#


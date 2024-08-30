#
# @lc app=leetcode id=2699 lang=python3
# @lcpr version=
#
# [2699] Modify Graph Edge Weights
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappop, heappush
from typing import List


# TODO: https://leetcode.cn/problems/modify-graph-edge-weights/solutions/2279106/python3c-er-fen-dijkstra-by-steven2018-20vq/
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        e = [[] for _ in range(n)]
        idx = {}
        cnt = 0
        for i, (u, v, w) in enumerate(edges):
            e[u].append((v, w, i))
            e[v].append((u, w, i))
            if w == -1:
                idx[i] = cnt
                cnt += 1
        
        def check(x: int) -> int:
            dist = [inf] * n
            dist[source] = 0
            q = [(0, source)]
            while q:
                cost, u = heappop(q)
                if cost > dist[u]:
                    continue
                for v, w, i in e[u]:
                    # 关键代码：均匀分配+1操作
                    d = dist[u] + w if w != -1 else dist[u] + (x + idx[i]) // cnt
                    if d < dist[v]:
                        dist[v] = d
                        heappush(q, (d, v))
            return dist[destination]
        
        left, right = cnt, 2 * 10 ** 9 * cnt
        if check(left) > target or check(right) < target:
            return []
        
        ans = left
        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= target:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        
        for i in range(len(edges)):
            if edges[i][2] == -1:
                edges[i][2] = (ans + idx[i]) // cnt
        return edges


        
# @lc code=end



#
# @lcpr case=start
# 5\n[[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]\n0\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,-1],[0,2,5]]\n0\n2\n6\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]\n0\n2\n6\n
# @lcpr case=end

#


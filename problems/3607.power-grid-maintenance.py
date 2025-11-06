#
# @lc app=leetcode id=3607 lang=python3
#
# [3607] Power Grid Maintenance
#

# @lc code=start
import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = c + 1
        mat = [[0] * n for _ in range(n)]
        for a, b in connections:
            mat[a][b] = 1
            mat[b][a] = 1
        active_status = [1] * n
        ans = []
        for event_type, node in queries:
            match event_type:
                case 1:
                    if active_status[node]:
                        ans.append(node)
                    else:
                        que = [node]
                        min_node = n
                        visited = [0] * n
                        while que:
                            node = que.pop(0)
                            if visited[node]:
                                continue
                            visited[node] = 1
                            if active_status[node]:
                                min_node = min(min_node, node)
                            for next_node in range(n):
                                if mat[node][next_node]:
                                    que.append(next_node)
                        ans.append(min_node if min_node != n else -1)
                case 2:
                    active_status[node] = 0
        return ans
    
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = c + 1
        mat = [[0] * n for _ in range(n)]
        for a, b in connections:
            mat[a][b] = 1
            mat[b][a] = 1
        for i in range(n):
            mat[i][i] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] == 1 and mat[k][j] == 1:
                        mat[i][j] = 1
        
        sl = SortedList(range(1,n))

        ans = []

        for event_type, node in queries:
            match event_type:
                case 1:
                    if node in sl:
                        ans.append(node)
                    else:
                        for v in sl:
                            if mat[node][v]:
                                ans.append(v)
                                break
                        else:
                            ans.append(-1)
                case 2:
                    if node in sl:
                        sl.remove(node)
        return ans
    
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(c + 1)]
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        heaps = []

        def dfs(x: int) -> None:
            belong[x] = len(heaps) 
            h.append(x)
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] >= 0:
                continue
            h = []
            dfs(i)
            heapq.heapify(h)
            heaps.append(h)

        ans = []
        offline = [False] * (c + 1)
        for op, x in queries:
            if op == 2:
                offline[x] = True
                continue
            if not offline[x]:
                ans.append(x)
                continue
            h = heaps[belong[x]]
            while h and offline[h[0]]:
                heapq.heappop(h)
            ans.append(h[0] if h else -1)
        return ans






# @lc code=end

# print(
#     Solution().processQueries(
#         c = 4,
#         connections=[[2,3],[1,3],[4,1],[3,4]],
#         queries=[[1,2],[2,4],[2,1],[1,4],[2,1],[1,1],[2,2],[1,4],[2,1],[2,2],[2,3],[2,4],[2,1],[1,1],[2,3],[2,2],[2,3],[1,4],[2,4]],
#     )
# )
print(
    Solution().processQueries(
        c = 4,
        connections=[[1,4]],
        queries=[[2,4],[2,2],[2,2],[1,2],[1,3],[1,4],[2,1],[1,1],[1,3],[2,2],[1,4],[2,2],[2,4],[1,4],[1,2]],
    )
)
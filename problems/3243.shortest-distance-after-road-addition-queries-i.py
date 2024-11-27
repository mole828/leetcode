#
# @lc app=leetcode id=3243 lang=python3
# @lcpr version=
#
# [3243] Shortest Distance After Road Addition Queries I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import numpy as np

# Time Limit Exceeded, 956 / 972 testcases passed
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mat = np.full((n, n), np.inf)
        np.fill_diagonal(mat, 0)
        for i in range(n-1):
            mat[i, i+1] = 1
            
        def floyd_warshall():
            for k in range(n):
                mat[:] = np.minimum(mat, mat[:, k, np.newaxis] + mat[np.newaxis, k, :])

        floyd_warshall()
        result = []
        for i, j in queries:
            mat[i, j] = 1
            floyd_warshall()
            result.append(int(mat[0][-1]))

        return result


from collections import deque

class Solution:
    def bfs(self, start, end, n, graph):
        dist = [float('inf')] * n
        dist[start] = 0
        q = deque([start])

        while q:
            curr = q.popleft()
            for u in graph[curr]:
                if dist[u] > dist[curr] + 1:
                    dist[u] = dist[curr] + 1
                    q.append(u)

        return dist[end]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        graph = [[] for _ in range(n)]

        for i in range(n - 1):
            graph[i].append(i + 1)

        for u, v in queries:
            graph[u].append(v)
            answer.append(self.bfs(0, n - 1, n, graph))

        return answer
        
# @lc code=end

print(Solution().shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]]))

#
# @lcpr case=start
# 5\n[[2,4],[0,2],[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,3],[0,2]]\n
# @lcpr case=end

#


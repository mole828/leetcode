from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces

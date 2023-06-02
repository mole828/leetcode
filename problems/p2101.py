from collections import defaultdict
from typing import List
import numpy as np


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, ans, graph = len(bombs), 0, defaultdict(list)
        for a in range(n):
            for b in range(a+1,n):
                xa,ya,ra = bombs[a]
                xb,yb,rb = bombs[b]
                widthSq = (xa-xb)**2 + (ya-yb)**2
                if widthSq <= ra**2:graph[a].append(b)
                if widthSq <= rb**2:graph[b].append(a)

        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans
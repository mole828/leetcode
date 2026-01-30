#
# @lc app=leetcode id=2977 lang=python3
#
# [2977] Minimum Cost to Convert String II
#

# @lc code=start
import heapq
from typing import List

import numpy as np


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mat = np.full((26, 26), np.inf)
        np.fill_diagonal(mat, 0)
        def n(s:str):
            return ord(s)-ord('a')
        for a,b,_cost in zip(original, changed, cost):
            mat[n(a)][n(b)] = min(_cost, mat[n(a)][n(b)])
        for k in range(26):
            mat = np.minimum(mat, mat[:,k,None] + mat[None,k,:])
        result = sum(mat[n(a)][n(b)] for a,b in zip(source,target))
        return -1 if result==np.inf else int(result)


import numpy as np
from functools import lru_cache

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        def diff(s: str) -> int:
            return sum(
                1 if a != b else 0
                for a, b in zip(s, target)
            )
        
        heap: list[tuple[int, int, str]] = []
        heapq.heappush(heap, (diff(source), 0, source))
        has_seen: dict[str, int] = {}

        while heap:
            _, cost_now, s = heapq.heappop(heap)
            if s in has_seen:
                continue
            has_seen[s] = cost_now
            if s == target:
                return cost_now
            for o, c, co in zip(original, changed, cost):
                ns = s.replace(o, c)
                if ns in has_seen:
                    continue
                heapq.heappush(heap, (diff(ns) + cost_now + co, cost_now + co, ns))
        return -1
    
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall, shortest_path
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nodes = {s:i for i, s in enumerate(set(original + changed))}

        m = len(nodes)
        n = len(source)
        adj = [[float('inf')]*m for _ in range(m)]
        for x,y,w in zip(original, changed, cost):
            u, v = nodes[x], nodes[y]
            adj[u][v] = min(adj[u][v], w)
        
        changed = set(changed)
        original = set(original)
        original_len = set(len(s) for s in original)
        
        dist = floyd_warshall(csr_matrix(adj), directed=True)
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            if source[i-1] == target[i-1]:
                dp[i] = dp[i-1]
            for length in original_len:
                if i>=length and (s:= source[i-length:i]) in original and (t:= target[i-len(s):i]) in changed:
                    dp[i] = min(dp[i], dp[i-len(s)] + dist[nodes[s],nodes[t]])
                
        
        return -1 if dp[-1] == float('inf') else int(dp[-1])

# @lc code=end

if __name__ == "__main__":
    print(Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))
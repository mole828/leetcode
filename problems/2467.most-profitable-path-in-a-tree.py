#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
from typing import List
from math import inf


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        bob_time = [n] * n 
        def dfs_bob(x: int, fa: int, t: int) -> bool:
            if x == 0:
                bob_time[x] = t
                return True
            for y in g[x]:
                if y != fa and dfs_bob(y, x, t + 1):
                    bob_time[x] = t 
                    return True
            return False
        dfs_bob(bob, -1, 0)

        g[0].append(-1)
        ans = -inf
        def dfs_alice(x: int, fa: int, alice_time: int, tot: int) -> None:
            if alice_time < bob_time[x]:
                tot += amount[x]
            elif alice_time == bob_time[x]:
                tot += amount[x] // 2
            if len(g[x]) == 1: 
                nonlocal ans
                ans = max(ans, tot)  
                return
            for y in g[x]:
                if y != fa:
                    dfs_alice(y, x, alice_time + 1, tot)
        dfs_alice(0, -1, 0, 0)
        return ans

        
                    
        
# @lc code=end

print(Solution().mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))  # 6
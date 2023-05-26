from functools import cache
from typing import List

'''
2023.5.26 second time
'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2,-1,-1): piles[i] += piles[i+1]
        print(piles)
        @cache
        def dfs(i, M):
            if i + 2 * M >= n: return piles[i] # 可以全拿时返回
            return max(piles[i] - dfs(i+j, max(M,j)) for j in range(1, 2*M+1))
        return dfs(0, 1)
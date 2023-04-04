from cmath import inf
from functools import cache
from typing import List

'''
TODO
'''


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache
        def f(l, r, p):
            print(f"f({l},{r},{p})")
            if l > r:
                return 0 if p == 0 else inf
            if p == 0:
                return inf
            if l == r:
                return 0 if p == 1 else inf
            if p == 1:
                return sum(stones[l:r+1]) + min(f(l,i,1) + f(i + 1,r,k-1) for i in range(l, r))
            return min(f(l,i,1) + f(i+1,r,p-1) for i in range(l, r))
        ans = f(0, len(stones) - 1, 1)
        return -1 if ans == inf else ans
    
if __name__ == '__main__':
    Solution().mergeStones(stones = [3,2,4,1], k = 2)
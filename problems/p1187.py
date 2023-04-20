from bisect import bisect_right
from functools import cache
from math import inf
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dfs(i: int, pre: int) -> int:
            if i == len(arr1): return 0
            res = inf
            pos = bisect_right(arr2, pre)
            if pos < len(arr2):
                res = dfs(i + 1, arr2[pos]) + 1

            if arr1[i] > pre:
                res = min(res, dfs(i + 1, arr1[i]))
            return res
        
        ans = dfs(0, -1)
        return ans if ans != inf else -1
    
if __name__ == '__main__':
    assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])==1
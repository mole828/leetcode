from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n,pre=len(nums),[0]
        for i in nums:pre.append(pre[-1]+i)
        @cache
        def dfs(i:int,z:int):
            if z>i or i==0:return 0
            if z==1:return pre[i]/i
            return max(dfs(j,z-1)+(pre[i]-pre[j])/(i-j) for j in range(i-1,-1,-1))
        return dfs(n,k)

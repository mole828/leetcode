#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        s = set(arr)
        print(arr)
        @cache 
        def f(i: int):
            ans = 1
            for j in arr:
                if j > i**0.5:
                    break 
                if i % j == 0 and i // j in s:
                    if i // j == j:
                        ans += f(j) * f(j)
                    else:
                        ans += f(j) * f(i//j) * 2
            return ans
        return sum(
            f(i) for i in arr
        ) % (10**9 + 7)
# @lc code=end

print(Solution().numFactoredBinaryTrees(
    [2,4,5,10]
))

print(Solution().numFactoredBinaryTrees(
    [18,3,6,2]
))
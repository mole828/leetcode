#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
from collections import Counter
from functools import cache
from typing import List

MOD = 1_000_000_007
SIZE = 26

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        arr = [0] * 26
        ord_a = ord('a')
        for c in s:
            arr[ord(c) - ord_a] += 1
        for tick in range(t):
            new_arr = [0] * SIZE
            for j in range(26):
                arr_j = arr[j] % MOD
                for k in range(nums[j]):
                    new_arr[(j+k+1) % SIZE] += arr_j
            arr = new_arr
        return sum(arr) % MOD
    

class Solution:
    # Memory Limit Exceeded, 529/536 cases passed
    # 存全部的 map 过大, 只能用后续的方法
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10**9)
        @cache
        def f(x: int, t: int) -> int:
            if t == 0:
                return 1
            return sum(
                f((x+d+1)%SIZE, t-1)
                for d in range(nums[x])
            ) % MOD
        return sum(
            f(ord(c) - ord('a'), t)
            for c in s
        ) % MOD

import numpy as np

# a^n @ f0
def pow_mul(a: np.ndarray, n: int, f0: np.ndarray) -> np.ndarray:
    res = f0
    while n:
        if n & 1:
            res = a @ res % MOD
        a = a @ a % MOD
        n >>= 1
    return res

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        f0 = np.ones((SIZE,), dtype=object)
        m = np.zeros((SIZE, SIZE), dtype=object)
        for i, c in enumerate(nums):
            for j in range(i + 1, i + c + 1):
                m[i, j % SIZE] = 1
        mt = pow_mul(m, t, f0)

        ans = 0
        for ch, cnt in Counter(s).items():
            ans += mt[ord(ch) - ord('a')] * cnt
        return ans % MOD
# @lc code=end

print(Solution().lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
print(Solution().lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
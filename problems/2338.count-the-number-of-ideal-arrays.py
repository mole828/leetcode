#
# @lc app=leetcode id=2338 lang=python3
#
# [2338] Count the Number of Ideal Arrays
#

# @lc code=start
from functools import cache
from typing import Optional

MOD = 10**9+7

class Solution:
    # Time Limit Exceeded, 31/47 cases passed (N/A)
    def idealArrays(self, n: int, maxValue: int) -> int:
        @cache
        def dfs(last_n: int, has: tuple):
            if last_n == 0:
                return 1
            total = 0
            for i in range(has[-1], maxValue+1):
                pass_flag = True
                for j in has:
                    if i % j != 0:
                        pass_flag = False
                        break
                    
                if pass_flag:
                    new_has_set = set(has+(i,))
                    new_has = tuple(new_has_set)
                    total += dfs(last_n-1, new_has)
            return total
        total = 0
        for i in range(1, maxValue+1):
            total += dfs(n-1, (i,))
            
        return total
                
class Solution:
    # Memory Limit Exceeded, 35/47 cases passed (N/A)
    def idealArrays(self, n: int, maxValue: int) -> int:
        @cache
        def dfs(last_size: int, last_value: int) -> int:
            if last_size == 0:
                return 1
            total = 0
            for i in range(last_value, maxValue+1, last_value):
                total += dfs(last_size-1, i)
            return total % MOD
        return dfs(n, 1)

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        c = [[0] * 16 for _ in range(n)]
        mod = 10**9 + 7
        for i in range(n):
            for j in range(min(16, i + 1)):
                c[i][j] = 1 if j == 0 else (c[i - 1][j] + c[i - 1][j - 1]) % mod
        f = [[0] * 16 for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            f[i][1] = 1
        for j in range(1, 15):
            for i in range(1, maxValue + 1):
                k = 2
                while k * i <= maxValue:
                    f[k * i][j + 1] = (f[k * i][j + 1] + f[i][j]) % mod
                    k += 1
        ans = 0
        for i in range(1, maxValue + 1):
            for j in range(1, 16):
                ans = (ans + f[i][j] * c[-1][j - 1]) % mod
        return ans



# @lc code=end

print(Solution().idealArrays(n = 2, maxValue = 5))
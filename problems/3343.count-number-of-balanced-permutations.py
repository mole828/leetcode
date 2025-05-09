#
# @lc app=leetcode id=3343 lang=python3
#
# [3343] Count Number of Balanced Permutations
#

# @lc code=start

# 链接：https://leetcode.cn/problems/count-number-of-balanced-permutations/solutions/2975507/duo-zhong-ji-pai-lie-shu-ji-shu-dppython-42ky/

from functools import cache
from itertools import accumulate


MOD = 1_000_000_007
MX = 41

fac = [0] * MX  # f[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cnt = [0] * 10
        total = 0
        for c in map(int, num):
            cnt[c] += 1
            total += c

        if total % 2:
            return 0

        pre = list(accumulate(cnt))

        @cache
        def dfs(i: int, left1: int, left_s: int) -> int:
            if i < 0:
                return 1 if left_s == 0 else 0
            res = 0
            c = cnt[i]
            left2 = pre[i] - left1
            for k in range(max(c - left2, 0), min(c, left1) + 1):
                if k * i > left_s:
                    break
                r = dfs(i - 1, left1 - k, left_s - k * i)
                res += r * inv_f[k] * inv_f[c - k]
            return res % MOD

        n = len(num)
        n1 = n // 2
        return fac[n1] * fac[n - n1] * dfs(9, n1, total // 2) % MOD

# @lc code=end

print(Solution().countBalancedPermutations("112"))
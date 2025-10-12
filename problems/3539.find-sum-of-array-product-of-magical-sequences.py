#
# @lc app=leetcode id=3539 lang=python3
# @lcpr version=30204
#
# [3539] Find Sum of Array Product of Magical Sequences
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


MOD = 1_000_000_007
MX = 31

fac = [0] * MX  # fac[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        pow_v = [[1] * (m + 1) for _ in range(n)]
        for i, v in enumerate(nums):
            for j in range(1, m + 1):
                pow_v[i][j] = pow_v[i][j - 1] * v % MOD

        @cache
        def dfs(i: int, left_m: int, x: int, left_k: int) -> int:
            c1 = x.bit_count()
            if c1 + left_m < left_k:  # 可行性剪枝
                return 0
            if i == n or left_m == 0 or left_k == 0:  # 无法继续选数字
                return 1 if left_m == 0 and c1 == left_k else 0
            res = 0
            for j in range(left_m + 1):  # 枚举 I 中有 j 个下标 i
                # 这 j 个下标 i 对 S 的贡献是 j * pow(2, i)
                # 由于 x = S >> i，转化成对 x 的贡献是 j
                bit = (x + j) & 1  # 取最低位，提前从 left_k 中减去，其余进位到 x 中
                r = dfs(i + 1, left_m - j, (x + j) >> 1, left_k - bit)
                res += r * pow_v[i][j] * inv_f[j]
            return res % MOD

        return dfs(0, m, 0, k) * fac[m] % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-sum-of-array-product-of-magical-sequences/solutions/3668501/duo-wei-dp-zu-he-shu-xue-by-endlesscheng-j6y8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end



#
# @lcpr case=start
# 5\n5\n[1,10,100,10000,1000000]\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n[5,4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n[28]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#

# @lc code=start
from functools import reduce
from typing import List

MOD = 10 ** 9 + 7
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        while n > 0:
            # bin(-n) 是补码表示，-n = ~n + 1
            # 所以 n & -n 就是 n 中最低位的 1 对应的数
            # 比如 n = 10 = 1010, -n = ~1010 + 1 = 0101 + 1 = 0110
            # 所以 n & -n = 1010 & 0110 = 0010
            powers.append(n & -n)
            n -= n & -n
        res = []
        for l, r in queries:
            sub = powers[l:r + 1]
            res.append(
                reduce(lambda x, y: x * y, sub) % MOD
            )
        return res

        
# @lc code=end

print(Solution().productQueries(15, [[0,1],[2,2],[0,3]]))
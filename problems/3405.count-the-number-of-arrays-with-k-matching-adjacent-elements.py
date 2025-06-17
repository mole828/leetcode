#
# @lc app=leetcode id=3405 lang=python3
#
# [3405] Count the Number of Arrays with K Matching Adjacent Elements
#

# @lc code=start

from math import comb

MOD = 1_000_000_007

# 纯数学题
# https://leetcode.cn/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/3033292/chun-shu-xue-ti-pythonjavacgo-by-endless-mxj7/
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n - 1, k) % MOD * m * pow(m - 1, n - k - 1, MOD) % MOD
# @lc code=end


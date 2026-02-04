#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
from itertools import pairwise
from typing import List

from numpy import inf


# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = f1 = f2 = f3 = -inf
        for x, y in pairwise(nums):
            f3 = max(f3, f2) + y if x < y else -inf
            f2 = max(f2, f1) + y if x > y else -inf
            f1 = max(f1, x)  + y if x < y else -inf
            ans = max(ans, f3)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/trionic-array-ii/solutions/3741020/fen-zu-xun-huan-on-shi-jian-o1-kong-jian-ewr5/
        
# @lc code=end


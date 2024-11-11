#
# @lc app=leetcode id=2601 lang=python3
# @lcpr version=
#
# [2601] Prime Subtraction Operation
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left
from typing import List

# link: https://leetcode.cn/problems/prime-subtraction-operation/solutions/2191560/jian-ji-xie-fa-shai-zhi-shu-er-fen-cha-z-wj7i/

MX = 1000
P = [0]  # 哨兵，避免二分越界
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        P.append(i)  # 预处理质数列表
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            if x <= pre: return False
            pre = x - P[bisect_left(P, x - pre) - 1]  # 减去 < x-pre 的最大质数
        return True

# @lc code=end



#
# @lcpr case=start
# [4,9,6,10]\n
# @lcpr case=end

# @lcpr case=start
# [6,8,11,12]\n
# @lcpr case=end

# @lcpr case=start
# [5,8,3]\n
# @lcpr case=end

#


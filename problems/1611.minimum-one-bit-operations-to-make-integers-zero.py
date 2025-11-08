#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
import math


@cache
def bto0(b): 
    return (1<<b+1) - 1

@cache
def nto0(n):
    if n == 0: return 0
    b1 = int(math.log2(n))
    return bto0(b1) - nto0(n - (1<<b1))

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return nto0(n)
# @lc code=end

print(Solution().minimumOneBitOperations(9))

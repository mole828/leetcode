#
# @lc app=leetcode id=1545 lang=python3
# @lcpr version=
#
# [1545] Find Kth Bit in Nth Binary String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str:
            return "".join("1" if c == "0" else "0" for c in s)

        def reverse(s: str) -> str:
            return s[::-1]

        @cache
        def get(n: int) -> str:
            if n == 1:
                return "0"
            else:
                return get(n - 1) + "1" + reverse(invert(get(n - 1)))
            
        return get(n)[k - 1]
# @lc code=end



#
# @lcpr case=start
# 3\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n11\n
# @lcpr case=end

#


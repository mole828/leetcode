#
# @lc app=leetcode id=3133 lang=python3
# @lcpr version=30204
#
# [3133] Minimum Array End
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # bit_x = [0] * 32
        # for i,c in enumerate(bin(x)[2:][::-1]):
        #     bit_x[i] = int(c)
        # bit = bit_x[:]
        y = x
        while n:
            if y & x == x:
                n -= 1
            y += 1

        return y - 1
    

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        pos = 0
        n -= 1
        while n > 0:
            bit = n & 1
            n = n >> 1
            while x & (1 << pos) > 0:
                pos += 1
            x = x ^ bit << pos
            pos += 1
        return x


# @lc code=end



#
# @lcpr case=start
# 3\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n7\n
# @lcpr case=end

#


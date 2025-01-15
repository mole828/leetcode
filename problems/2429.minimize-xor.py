#
# @lc app=leetcode id=2429 lang=python3
# @lcpr version=
#
# [2429] Minimize XOR
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1 = num1.bit_count()
        c2 = num2.bit_count()
        while c2 < c1:
            num1 &= num1 - 1  # 最低的 1 变成 0
            c2 += 1
        while c2 > c1:
            num1 |= num1 + 1  # 最低的 0 变成 1
            c2 -= 1
        return num1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimize-xor/solutions/1864059/o1-kong-jian-fu-za-du-zuo-fa-by-endlessc-ywio/
# @lc code=end



#
# @lcpr case=start
# 3\n5\n
# @lcpr case=end

# @lcpr case=start
# 1\n12\n
# @lcpr case=end

#


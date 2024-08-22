#
# @lc app=leetcode id=476 lang=python3
# @lcpr version=
#
# [476] Number Complement
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans

# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


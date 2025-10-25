#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# HACK: 可以优化
class Solution:
    def totalMoney(self, n: int) -> int:
        output = 0
        for week in range(1,200):
            for day in range(7):
                output += week+day 
                n -= 1
                if not n :
                    return output
        return 0

# @lc code=end


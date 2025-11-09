#
# @lc app=leetcode id=2169 lang=python3
# @lcpr version=30204
#
# [2169] Count Operations to Obtain Zero
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        steps = 0
        while num1 and num2:
            if num1 >= num2:
                steps += num1 // num2
                num1 = num1 % num2
            else:
                steps += num2 // num1
                num2 = num2 % num1
        return steps
# @lc code=end



#
# @lcpr case=start
# 2\n3\n
# @lcpr case=end

# @lcpr case=start
# 10\n10\n
# @lcpr case=end

#


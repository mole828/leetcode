#
# @lc app=leetcode id=1323 lang=python3
# @lcpr version=30204
#
# [1323] Maximum 69 Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6':
                num = num[:i] + '9' + num[i+1:]
                break
        return int(num)
# @lc code=end



#
# @lcpr case=start
# 9669\n
# @lcpr case=end

# @lcpr case=start
# 9996\n
# @lcpr case=end

# @lcpr case=start
# 9999\n
# @lcpr case=end

#


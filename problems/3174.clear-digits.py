#
# @lc app=leetcode id=3174 lang=python3
# @lcpr version=30204
#
# [3174] Clear Digits
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        num_chars = set("0123456789")
        stack = []
        for c in s:
            if c in num_chars and stack and stack[-1] not in num_chars:
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)
                
# @lc code=end



#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "cb34"\n
# @lcpr case=end

#


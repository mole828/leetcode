#
# @lc app=leetcode id=2116 lang=python3
# @lcpr version=30204
#
# [2116] Check if a Parentheses String Can Be Valid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        def check(s, locked, open_parenthesis):
            balance = 0
            for ch, l in zip(s, locked):
                if ch == open_parenthesis or l == '0':
                    balance += 1
                else:
                    balance -= 1
                    if balance < 0:
                        return False
            return True

        return len(s)%2 == 0 and check(s, locked, '(') and check(reversed(s), reversed(locked), ')')
# @lc code=end



#
# @lcpr case=start
# "))()))"\n"010100"\n
# @lcpr case=end

# @lcpr case=start
# "()()"\n"0000"\n
# @lcpr case=end

# @lcpr case=start
# ")"\n"0"\n
# @lcpr case=end

#


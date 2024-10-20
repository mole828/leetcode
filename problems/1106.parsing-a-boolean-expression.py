#
# @lc app=leetcode id=1106 lang=python3
# @lcpr version=
#
# [1106] Parsing A Boolean Expression
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def n(v: bool): # not
            return not v
        def a(*args: list[bool]) -> bool: # and
            return all(args)
        def o(*args: list[bool]) -> bool: # or
            return any(args)
        f = False
        t = True
        s = expression.replace("!", "n")
        s = s.replace("&", "a")
        s = s.replace("|", "o")
        return eval(s)
# @lc code=end



#
# @lcpr case=start
# "&(|(f))"\n
# @lcpr case=end

# @lcpr case=start
# "|(f,f,f,t)"\n
# @lcpr case=end

# @lcpr case=start
# "!(&(f,t))"\n
# @lcpr case=end

#


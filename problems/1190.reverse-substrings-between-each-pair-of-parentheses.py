#
# @lc app=leetcode id=1190 lang=python3
# @lcpr version=
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack:list[str] = []
        for c in s:
            if c == ')':
                sub = []
                while (cc:=stack.pop())!='(' :
                    sub.append(cc)
                stack += sub
                continue
            stack.append(c)
        return ''.join(stack)
# @lc code=end

print(Solution().reverseParentheses("(ed(et(oc))el)"))

#
# @lcpr case=start
# "(abcd)"\n
# @lcpr case=end

# @lcpr case=start
# "(u(love)i)"\n
# @lcpr case=end

# @lcpr case=start
# "(ed(et(oc))el)"\n
# @lcpr case=end

#


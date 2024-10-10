#
# @lc app=leetcode id=921 lang=python3
# @lcpr version=
#
# [921] Minimum Add to Make Parentheses Valid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ans += 1
        return ans + cnt
# @lc code=end



#
# @lcpr case=start
# "())"\n
# @lcpr case=end

# @lcpr case=start
# "((("\n
# @lcpr case=end

#


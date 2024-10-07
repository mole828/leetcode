#
# @lc app=leetcode id=2696 lang=python3
# @lcpr version=
#
# [2696] Minimum String Length After Removing Substrings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and (stack[-1] == 'A' and c == 'B' or stack[-1] == 'C' and c == 'D'):
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
# @lc code=end



#
# @lcpr case=start
# "ABFCACDB"\n
# @lcpr case=end

# @lcpr case=start
# "ACBBD"\n
# @lcpr case=end

#


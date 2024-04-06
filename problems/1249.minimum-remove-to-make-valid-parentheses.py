#
# @lc app=leetcode id=1249 lang=python3
# @lcpr version=
#
# [1249] Minimum Remove to Make Valid Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left: list[int] = []
        wait_remove:list[int] = []
        for i,char in enumerate(s):
            if char == '(':
                left.append(i) 
            if char == ')':
                if left:
                    left.pop() 
                else:
                    wait_remove.append(i)
        wait_remove += left 
        wait_remove.sort()
        while wait_remove:
            i = wait_remove.pop() 
            s = s[:i] + s[i+1:]
        return s
# @lc code=end

print(Solution().minRemoveToMakeValid('lee(t(c)o)de)'))
print(Solution().minRemoveToMakeValid('))(('))

#
# @lcpr case=start
# "lee(t(c)o)de)"\n
# @lcpr case=end

# @lcpr case=start
# "a)b(c)d"\n
# @lcpr case=end

# @lcpr case=start
# "))(("\n
# @lcpr case=end

#


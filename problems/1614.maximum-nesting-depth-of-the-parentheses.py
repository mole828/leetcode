#
# @lc app=leetcode id=1614 lang=python3
# @lcpr version=
#
# [1614] Maximum Nesting Depth of the Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0 
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth
        
# @lc code=end



#
# @lcpr case=start
# "(1+(2*3)+((8)/4))+1"\n
# @lcpr case=end

# @lcpr case=start
# "(1)+((2))+(((3)))"\n
# @lcpr case=end

#


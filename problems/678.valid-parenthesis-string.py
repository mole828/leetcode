#
# @lc app=leetcode id=678 lang=python3
# @lcpr version=
#
# [678] Valid Parenthesis String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0 
        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False 
            left_min = max(left_min,0) 
        return left_min == 0
# @lc code=end

print(Solution().checkValidString(
'''
(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())
'''.replace('\n','')
))

#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "(*)"\n
# @lcpr case=end

# @lcpr case=start
# "(*))"\n
# @lcpr case=end

#


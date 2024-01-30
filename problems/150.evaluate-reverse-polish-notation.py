#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    operators = ['+','-','*','/']
    def evalRPN(self, tokens: List[str]) -> int:
        value_stack = []
        while tokens:
            token = tokens.pop(0)
            if token in Solution.operators:
                a, b = value_stack.pop(), value_stack.pop()
                op = f"{b}{token}{a}"
                value_stack.append(int(
                    eval(op)
                ))
                # print(op,eval(op))
            else:
                value_stack.append(int(token))
            # print(value_stack)
        return value_stack[0]
        
# @lc code=end

print(Solution().evalRPN(tokens = ["2","1","+","3","*"]))
print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))
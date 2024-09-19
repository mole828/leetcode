#
# @lc app=leetcode id=241 lang=python3
# @lcpr version=
#
# [241] Different Ways to Add Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
import operator
import re
from typing import List

# link https://leetcode.cn/problems/different-ways-to-add-parentheses/solutions/1636736/by-himymben-90tl/
OP_MAP = {"+": operator.add, "-": operator.sub, "*": operator.mul}
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dfs(left: int, right: int) -> List[int]:
            if left == right:
                return [int(sp[left])]
            res = []
            for i in range(left + 1, right, 2):
                for left_set in dfs(left, i - 1):
                    for right_set in dfs(i + 1, right):
                        res.append(OP_MAP[sp[i]](left_set, right_set))
            return res

        sp = re.split(r"(\D)", expression)
        return list(dfs(0, len(sp) - 1))
# @lc code=end



#
# @lcpr case=start
# "2-1-1"\n
# @lcpr case=end

# @lcpr case=start
# "2*3-4*5"\n
# @lcpr case=end

#


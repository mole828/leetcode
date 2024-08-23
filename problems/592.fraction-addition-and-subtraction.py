#
# @lc app=leetcode id=592 lang=python3
# @lcpr version=
#
# [592] Fraction Addition and Subtraction
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from fractions import Fraction
import re


ptn = re.compile(r'[+-]?\d+/\d+')
class Solution:
    def fractionAddition(self, expr: str) -> str:
        res = sum(Fraction(f) for f in ptn.findall(expr))
        return f'{res.numerator}/{res.denominator}'
# @lc code=end



#
# @lcpr case=start
# "-1/2+1/2"\n
# @lcpr case=end

# @lcpr case=start
# "-1/2+1/2+1/3"\n
# @lcpr case=end

# @lcpr case=start
# "1/3-1/2"\n
# @lcpr case=end

#


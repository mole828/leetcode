#
# @lc app=leetcode id=633 lang=python3
# @lcpr version=
#
# [633] Sum of Square Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        has: set[int] = set()
        range_max = int(c**(1/2)+1)
        for i in range(0, range_max):
            ii = i**2
            target = c - ii
            has.add(ii)
            if target in has:
                return True
            
        return False
# @lc code=end

Solution().judgeSquareSum(5)

#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#


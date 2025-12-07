#
# @lc app=leetcode id=1523 lang=python3
# @lcpr version=30204
#
# [1523] Count Odd Numbers in an Interval Range
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
        
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 8\n10\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1051 lang=python3
# @lcpr version=
#
# [1051] Height Checker
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        after = sorted(heights)
        return sum(after[i]!=heights[i] for i in range(len(heights)))
# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#


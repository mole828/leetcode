#
# @lc app=leetcode id=2220 lang=python3
# @lcpr version=
#
# [2220] Minimum Bit Flips to Convert Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
# @lc code=end



#
# @lcpr case=start
# 10\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n4\n
# @lcpr case=end

#


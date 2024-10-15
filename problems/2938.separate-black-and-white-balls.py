#
# @lc app=leetcode id=2938 lang=python3
# @lcpr version=
#
# [2938] Separate Black and White Balls
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        swap, black = 0, 0
        for c in s:
            if c == "0":
                swap += black
            else:
                black += 1
        return swap
        
# @lc code=end



#
# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "100"\n
# @lcpr case=end

# @lcpr case=start
# "0111"\n
# @lcpr case=end

#


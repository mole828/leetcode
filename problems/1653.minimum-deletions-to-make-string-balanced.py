#
# @lc app=leetcode id=1653 lang=python3
# @lcpr version=
#
# [1653] Minimum Deletions to Make String Balanced
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = count = 0
        for c in s:
            if c == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1
        return res

# @lc code=end



#
# @lcpr case=start
# "aababbab"\n
# @lcpr case=end

# @lcpr case=start
# "bbaaaaabb"\n
# @lcpr case=end

#


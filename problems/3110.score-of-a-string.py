#
# @lc app=leetcode id=3110 lang=python3
# @lcpr version=
#
# [3110] Score of a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1,len(s)):
            score += abs(ord(s[i])-ord(s[i-1]))
        return score
# @lc code=end



#
# @lcpr case=start
# "hello"\n
# @lcpr case=end

# @lcpr case=start
# "zaz"\n
# @lcpr case=end

#


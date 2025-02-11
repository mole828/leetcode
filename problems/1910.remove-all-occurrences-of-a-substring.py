#
# @lc app=leetcode id=1910 lang=python3
# @lcpr version=30204
#
# [1910] Remove All Occurrences of a Substring
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s
# @lc code=end



#
# @lcpr case=start
# "daabcbaabcbc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "axxxxyyyyb"\n"xy"\n
# @lcpr case=end

#


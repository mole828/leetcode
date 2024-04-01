#
# @lc app=leetcode id=58 lang=python3
# @lcpr version=
#
# [58] Length of Last Word
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
# @lc code=end



#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end

#


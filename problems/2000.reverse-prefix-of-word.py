#
# @lc app=leetcode id=2000 lang=python3
# @lcpr version=
#
# [2000] Reverse Prefix of Word
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i = word.index(ch)
            prefix = word[:i+1]
            return ''.join(reversed(prefix)) + word[i+1:]
        return word
        
# @lc code=end



#
# @lcpr case=start
# "abcdefd"\n"d"\n
# @lcpr case=end

# @lcpr case=start
# "xyxzxe"\n"z"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"z"\n
# @lcpr case=end

#


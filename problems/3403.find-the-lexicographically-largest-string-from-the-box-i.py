#
# @lc app=leetcode id=3403 lang=python3
#
# [3403] Find the Lexicographically Largest String From the Box I
#

# @lc code=start
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        max_len = len(word) - numFriends + 1
        lex_largest = ""
        for left in range(len(word)):
            for right in range(left, min(left + max_len, len(word))):
                sub = word[left:right+1]
                # print({'sub':sub})
                if sub > lex_largest:
                    lex_largest = sub
                elif sub+'{' > lex_largest:
                    continue
                else:
                    break
        return lex_largest
        
# @lc code=end

print(Solution().answerString(word = "dbca", numFriends = 2))
print(Solution().answerString(word = "bif", numFriends = 2))
print(Solution().answerString(word = "aann", numFriends = 2))
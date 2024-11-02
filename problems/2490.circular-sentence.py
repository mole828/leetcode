#
# @lc app=leetcode id=2490 lang=python3
# @lcpr version=30204
#
# [2490] Circular Sentence
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][-1]!= words[(i+1)%len(words)][0]:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "leetcode exercises sound delightful"\n
# @lcpr case=end

# @lcpr case=start
# "eetcode"\n
# @lcpr case=end

# @lcpr case=start
# "Leetcode is cool"\n
# @lcpr case=end

#


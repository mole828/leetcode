#
# @lc app=leetcode id=1813 lang=python3
# @lcpr version=
#
# [1813] Sentence Similarity III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        l1, r1 = 0, len(words1) - 1
        l2, r2 = 0, len(words2) - 1

        while l1 <= r1 and l2 <= r2 and words1[l1] == words2[l2]:
            l1 += 1
            l2 += 1

        while l1 <= r1 and l2 <= r2 and words1[r1] == words2[r2]:
            r1 -= 1
            r2 -= 1

        return l1 > r1 or l2 > r2
        
# @lc code=end



#
# @lcpr case=start
# "My name is Haley"\n"My Haley"\n
# @lcpr case=end

# @lcpr case=start
# "of"\n"A lot of words"\n
# @lcpr case=end

# @lcpr case=start
# "Eating right now"\n"Eating"\n
# @lcpr case=end

#


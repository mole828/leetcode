#
# @lc app=leetcode id=506 lang=python3
# @lcpr version=
#
# [506] Relative Ranks
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def rank(i: int) -> str:
            if i == 0:
                return "Gold Medal"
            if i == 1:
                return "Silver Medal"
            if i == 2:
                return "Bronze Medal"
            return str(i+1)
        score_with_index:tuple[int,int] = []
        for k,v in enumerate(score):
            score_with_index.append((-v,k))
        score_with_index.sort()
        ranks = [''] * len(score)
        for k,v in enumerate(score_with_index):
            nag_score, i = v 
            ranks[i] = rank(k)
        return ranks

# @lc code=end



#
# @lcpr case=start
# [5,4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [10,3,8,9,4]\n
# @lcpr case=end

#


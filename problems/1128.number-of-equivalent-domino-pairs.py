#
# @lc app=leetcode id=1128 lang=python3
# @lcpr version=30204
#
# [1128] Number of Equivalent Domino Pairs
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [tuple(sorted(domino)) for domino in dominoes]
        count = Counter(dominoes)
        return sum(v * (v - 1) // 2 for v in count.values())
        
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,1],[3,4],[5,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,1],[1,2],[2,2]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1140 lang=python3
# @lcpr version=
#
# [1140] Stone Game II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2,-1,-1): piles[i] += piles[i+1]
        print(piles)
        @cache
        def dfs(i, M):
            if i + 2 * M >= n: return piles[i] # 可以全拿时返回
            return max(piles[i] - dfs(i+j, max(M,j)) for j in range(1, 2*M+1))
        return dfs(0, 1)
# @lc code=end



#
# @lcpr case=start
# [2,7,9,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,100]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1105 lang=python3
# @lcpr version=
#
# [1105] Filling Bookcase Shelves
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [np.inf] * (n + 1)
        dp[0] = 0
        for i, b in enumerate(books):
            curWidth = 0
            maxHeight = 0
            j = i
            while j >= 0:
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + maxHeight)
                j -= 1
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[2,4],[3,2]]\n6\n
# @lcpr case=end

#


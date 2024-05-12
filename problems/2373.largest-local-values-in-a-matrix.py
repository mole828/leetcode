#
# @lc app=leetcode id=2373 lang=python3
# @lcpr version=
#
# [2373] Largest Local Values in a Matrix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        matrix = np.matrix(grid, dtype=np.integer)
        result = np.zeros(shape=(n,n),dtype=np.integer)
        for i in range(n-2):
            for j in range(n-2):
                result[i+1][j+1] = np.max(matrix[i:i+3, j:j+3])
        return result[1:-1, 1:-1]
# @lc code=end



#
# @lcpr case=start
# [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]\n
# @lcpr case=end

#


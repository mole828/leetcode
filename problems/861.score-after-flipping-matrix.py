#
# @lc app=leetcode id=861 lang=python3
# @lcpr version=
#
# [861] Score After Flipping Matrix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        mat = np.mat(grid)
        print(mat)
        for row in range(mat.shape[0]):
            if not mat[row,0]:
                mat[row,:] = mat[row,:] ^ 1
        print(mat)
        mid = mat.shape[0] / 2
        for col in range(mat.shape[1]):
            if np.sum(mat[:,col]) < mid:
                mat[:,col] = mat[:,col] ^ 1
        print(mat)
        decimal_mat = [int(''.join(map(str, mat[i, :].tolist()[0])), 2) for i in range(mat.shape[0])]
        print(decimal_mat)
        return sum(decimal_mat)

# @lc code=end

print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
print(Solution().matrixScore([[0,1],[0,1],[0,1],[0,0]]))

#
# @lcpr case=start
# [[0,0,1,1],[1,0,1,0],[1,1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

#


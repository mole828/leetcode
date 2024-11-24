#
# @lc app=leetcode id=1975 lang=python3
# @lcpr version=30204
#
# [1975] Maximum Matrix Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mat = numpy.array(matrix)
        neg_count = numpy.sum(mat < 0)
        abs_mat = numpy.abs(mat)
        mat_sum = numpy.sum(abs_mat)
        print(neg_count, mat_sum)
        return int(mat_sum - numpy.min(abs_mat)*2 if neg_count % 2 else mat_sum)
        
# @lc code=end

print(Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))

#
# @lcpr case=start
# [[1,-1],[-1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[-1,-2,-3],[1,2,3]]\n
# @lcpr case=end

#


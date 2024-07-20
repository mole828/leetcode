#
# @lc app=leetcode id=1605 lang=python3
# @lcpr version=
#
# [1605] Find Valid Matrix Given Row and Column Sums
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0]*len(colSum) for _ in rowSum]
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if last:=min(colSum[x],rowSum[y]):
                    mat[y][x] = last
                    colSum[x] -= last
                    rowSum[y] -= last
        return mat
        
# @lc code=end

print(Solution().restoreMatrix([3,8],[4,7]))

#
# @lcpr case=start
# [3,8]\n[4,7]\n
# @lcpr case=end

# @lcpr case=start
# [5,7,10]\n[8,6,8]\n
# @lcpr case=end

#


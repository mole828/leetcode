#
# @lc app=leetcode id=1289 lang=python3
# @lcpr version=
#
# [1289] Minimum Falling Path Sum II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = grid.pop(0)
        while grid:
            next_row = grid.pop(0)
            for i in range(n):
                next_row[i] += min(row[j] for j in range(n) if j!=i)
            row = next_row
        return min(row)
# @lc code=end

print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))

#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[7]]\n
# @lcpr case=end

#


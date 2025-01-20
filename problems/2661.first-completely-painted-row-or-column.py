#
# @lc app=leetcode id=2661 lang=python3
# @lcpr version=
#
# [2661] First Completely Painted Row or Column
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row_last, col_last = [m]*n, [n]*m
        index: map[int, tuple[int,int]] = {}
        for y in range(n):
            for x in range(m):
                v = mat[y][x]
                index[v] = (y,x)
        for i, v in enumerate(arr):
            y,x = index[v]
            row_last[y] -= 1
            col_last[x] -= 1
            if not row_last[y] or not col_last[x]:
                return i
        raise ValueError()

        
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2]\n[[1,4],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [2,8,7,4,1,3,5,6,9]\n[[3,2,5],[1,4,6],[8,7,9]]\n
# @lcpr case=end

#


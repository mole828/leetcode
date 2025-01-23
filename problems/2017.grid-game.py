#
# @lc app=leetcode id=2017 lang=python3
# @lcpr version=
#
# [2017] Grid Game
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0] * n
        bottom = [0] * n
        for i in range(n):
            top[i] = top[i - 1] + grid[0][i]
            bottom[i] = bottom[i - 1] + grid[1][i]
        res = float('inf')
        for i in range(n):
            res = min(res, max(top[-1] - top[i], bottom[i - 1] if i > 0 else 0))
        return res
        
# @lc code=end



#
# @lcpr case=start
# [[2,5,4],[1,5,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,1],[8,5,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,1,15],[1,3,3,1]]\n
# @lcpr case=end

#


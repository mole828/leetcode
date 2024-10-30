#
# @lc app=leetcode id=2684 lang=python3
# @lcpr version=30204
#
# [2684] Maximum Number of Moves in a Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            if y == len(grid[0]) - 1:
                return 0

            result = 0

            for i in range(x - 1, x + 2):
                if 0 <= i < len(grid) and grid[i][y + 1] > grid[x][y]:
                    result = max(result, dfs(i, y + 1) + 1)

            return result

        return max(dfs(i, 0) for i in range(len(grid)))
# @lc code=end



#
# @lcpr case=start
# [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,2,4],[2,1,9],[1,1,7]]\n
# @lcpr case=end

#


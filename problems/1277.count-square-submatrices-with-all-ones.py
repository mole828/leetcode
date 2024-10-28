#
# @lc app=leetcode id=1277 lang=python3
# @lcpr version=30204
#
# [1277] Count Square Submatrices with All Ones
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans += dp[i][j]

        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,1,1,1],[1,1,1,1],[0,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#


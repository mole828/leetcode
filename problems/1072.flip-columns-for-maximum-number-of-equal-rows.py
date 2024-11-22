#
# @lc app=leetcode id=1072 lang=python3
# @lcpr version=
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Counter, List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())
# @lc code=end

print(Solution().maxEqualRowsAfterFlips([[0,1],[1,1]]))

#
# @lcpr case=start
# [[0,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[0,0,1],[1,1,0]]\n
# @lcpr case=end

#


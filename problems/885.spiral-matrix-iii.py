#
# @lc app=leetcode id=885 lang=python3
# @lcpr version=
#
# [885] Spiral Matrix III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [0, 1, 0, -1, 0]
        res = [[rStart, cStart]]
        j = n = 0
        while len(res) < rows * cols:
            for i in range(n // 2 + 1):
                rStart += directions[j]
                cStart += directions[j + 1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            n += 1
            j = (j + 1) % 4
        return res
# @lc code=end



#
# @lcpr case=start
# 1\n4\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n1\n4\n
# @lcpr case=end

#


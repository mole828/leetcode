#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#

# @lc code=start
from functools import cache

ROW = tuple[int, int, int]

class Solution:
    def numOfWays(self, n: int) -> int:
        colors = [0, 1, 2]
        @cache
        def numOfWaysWithLastRow(lastRow: ROW, thisN: int) -> int:
            if thisN == 0:
                return 1
            total = 0
            for c1 in colors:
                for c2 in colors:
                    if c2 == c1:
                        continue
                    for c3 in colors:
                        if c3 == c2:
                            continue
                        thisRow = (c1, c2, c3)
                        if thisRow[0] != lastRow[0] and thisRow[1] != lastRow[1] and thisRow[2] != lastRow[2]:
                            total += numOfWaysWithLastRow(thisRow, thisN - 1)
                            total %= 1_000_000_007
            return total
        return numOfWaysWithLastRow((-1, -1, -1), n)
        


# @lc code=end

print(Solution().numOfWays(1))  # Expected output: 12
print(Solution().numOfWays(2)) 
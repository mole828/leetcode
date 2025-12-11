#
# @lc app=leetcode id=3531 lang=python3
# @lcpr version=30204
#
# [3531] Count Covered Buildings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(SortedList)
        cols = defaultdict(SortedList)
        for r, c in buildings:
            rows[r].add(c)
            cols[c].add(r)
        covered = 0
        for row in rows.keys():
            col_list = rows[row]
            if len(col_list) > 2:
                for i in range(1, len(col_list) - 1):
                    v = col_list[i]
                    row_list = cols[v]
                    if row_list[0] < row and row_list[-1] > row:
                        covered += 1
        return covered

        
# @lc code=end



#
# @lcpr case=start
# 3\n[[1,2],[2,2],[3,2],[2,1],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,1],[1,2],[2,1],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,3],[3,2],[3,3],[3,5],[5,3]]\n
# @lcpr case=end

#


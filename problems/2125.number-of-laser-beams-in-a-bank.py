#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
from typing import List


class Solution(object):
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row_count = 0
        total = 0

        for row in bank:
            cur_row_count = sum(int(c) for c in row)
            if cur_row_count == 0:
                continue

            total += cur_row_count * prev_row_count
            prev_row_count = cur_row_count

        return total

    def numberOfBeams(self, bank: List[str]) -> int:
        ans = pre_cnt = 0
        for row in bank:
            cnt = row.count('1')
            if cnt > 0:
                ans += pre_cnt * cnt
                pre_cnt = cnt
        return ans
# @lc code=end


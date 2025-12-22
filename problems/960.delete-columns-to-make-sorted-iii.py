#
# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        @cache
        def can_append(col: int, last_col: int) -> bool:
            for row in range(len(strs)):
                if strs[row][col] < strs[row][last_col]:
                    return False
            return True
        @cache
        def dfs(col: int) -> int:
            if col == len(strs[0]):
                return 0
            keep = float('-inf')
            for next_col in range(col + 1, len(strs[0])):
                if can_append(next_col, col):
                    keep = max(keep, 1 + dfs(next_col))
            skip = dfs(col + 1)
            return max(keep, skip)
        max_keep = dfs(0)
        return len(strs[0]) - max_keep
# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minDeletionSize(["babca","bbazb"]))
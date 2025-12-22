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
        m = len(strs[0])
        f = [0] * m
        for i in range(m):
            for j in range(i):
                if f[j] > f[i] and all(s[j] <= s[i] for s in strs):
                    f[i] = f[j]
            f[i] += 1
        return m - max(f)

# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minDeletionSize(["babca","bbazb"]))
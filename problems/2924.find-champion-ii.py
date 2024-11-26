#
# @lc app=leetcode id=2924 lang=python3
# @lcpr version=
#
# [2924] Find Champion II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[tuple[int, int]]) -> int:
        in_digree = [0] * n
        for a, b in edges:
            in_digree[b] += 1
        if in_digree.count(0) > 1:
            return -1
        return in_digree.index(0)

# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,2],[1,3],[1,2]]\n
# @lcpr case=end

#


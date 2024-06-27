#
# @lc app=leetcode id=1791 lang=python3
# @lcpr version=
#
# [1791] Find Center of Star Graph
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e0, e1,  = edges[0], edges[1]
        return list(set(e0)&set(e1))[0]
# @lc code=end

print(Solution().findCenter([[1,2],[2,3],[4,2]]))

#
# @lcpr case=start
# [[1,2],[2,3],[4,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[5,1],[1,3],[1,4]]\n
# @lcpr case=end

#


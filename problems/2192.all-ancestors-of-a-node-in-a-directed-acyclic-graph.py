#
# @lc app=leetcode id=2192 lang=python3
# @lcpr version=
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from_set: list[set[int]] = [set() for i in range(n)]
        for a,b in edges:
            from_set[b].add(a)
        has_change = True
        while has_change:
            has_change = False
            for _set in from_set:
                add = set()
                for v in _set:
                    add.update(from_set[v])
                if add - _set:
                    has_change = True
                    _set.update(add)
        return [sorted(s) for s in from_set]
# @lc code=end



#
# @lcpr case=start
# 8\n[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]\n
# @lcpr case=end

#


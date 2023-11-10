#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjs = defaultdict(set)
        for i,j in adjacentPairs:
            adjs[i].add(j)
            adjs[j].add(i)

        for node,adj in adjs.items():
            if len(adj)==1:
                break
        ans = [node]

        while adjs[node]:
            new=adjs[node].pop()
            ans.append(new)
            adjs[new].remove(node)
            node=new
        return ans   
# @lc code=end

Solution().restoreArray([[2,1],[3,4],[3,2]])


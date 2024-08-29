#
# @lc app=leetcode id=947 lang=python3
# @lcpr version=
#
# [947] Most Stones Removed with Same Row or Column
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import collections
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)
        
        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)
        
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)
        
        return n - num
        
# @lc code=end



#
# @lcpr case=start
# [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[0,2],[1,1],[2,0],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0]]\n
# @lcpr case=end

#


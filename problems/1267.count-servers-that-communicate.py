#
# @lc app=leetcode id=1267 lang=python3
# @lcpr version=30204
#
# [1267] Count Servers that Communicate
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]
        vis = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    vis.append((i,j))
        ans = 0
        for i,j in vis:
            if row[i] > 1 or col[j] > 1:
                ans += 1

        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=2658 lang=python3
# @lcpr version=30204
#
# [2658] Maximum Number of Fish in a Grid
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        que = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    que.append((i, j))
        mat_sum = [[0] * m for _ in range(n)]
        has_meet: set[tuple[int,int]] = set()
        while que:
            i, j = que.pop()
            if (i, j) in has_meet:
                continue
            has_meet.add((i, j))
            this_meet = set()
            this_round = [(i,j)]
            while this_round:
                ii, jj = this_round.pop()
                if (ii, jj) in this_meet:
                    continue
                this_meet.add((ii, jj))
                has_meet.add((ii, jj))
                for ni, nj in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in this_meet and grid[ni][nj] != 0:
                        this_round.append((ni, nj))
            sum_fish = 0
            for ii, jj in this_meet:
                sum_fish += grid[ii][jj]
            for ii, jj in this_meet:
                mat_sum[ii][jj] = sum_fish
        return max(max(row) for row in mat_sum)

            

        
# @lc code=end



#
# @lcpr case=start
# [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]\n
# @lcpr case=end

#


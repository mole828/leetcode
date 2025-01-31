#
# @lc app=leetcode id=827 lang=python3
# @lcpr version=30204
#
# [827] Making A Large Island
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List, Optional


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        next_land_id = 1
        id_map: map[tuple[int,int], Optional[int]] = {}
        id_size: map[int, int] = defaultdict(int)
        def dfs(i: int, j: int, id: int = None) -> Optional[int]:
            if (i,j) in id_map:
                return id_map[(i,j)]
            value = grid[i][j]
            if value == 0:
                id_map[(i,j)] = None
                return None
            _id: int
            if id:
                _id = id
            else:
                nonlocal next_land_id
                _id = next_land_id
                next_land_id += 1
            id_map[(i,j)] = _id
            id_size[_id] += 1
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < n and 0 <= y < n:
                    if (x,y) not in id_map:
                        dfs(x,y,_id)
            return _id
        for i in range(n):
            for j in range(n):
                dfs(i,j)
        def reflect(i: int, j: int) -> int:
            if grid[i][j] == 1:
                return id_size[id_map[(i,j)]]
            else:
                ids = set()
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= x < n and 0 <= y < n:
                        if id_map[(x,y)]:
                            ids.add(id_map[(x,y)])
                return 1 + sum(id_size[_id] for _id in ids)
        res_mat = [[reflect(i,j) for j in range(n)] for i in range(n)]
        return max(max(row) for row in res_mat)
            

# @lc code=end



#
# @lcpr case=start
# [[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

#


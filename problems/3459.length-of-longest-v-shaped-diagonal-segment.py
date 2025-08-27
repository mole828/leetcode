#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from functools import cache
from typing import List, Optional


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def status(y: int, x: int):
            return 1 << (y * cols + x)
        que: List[tuple[int,int,int, Optional[tuple[int,int]], bool, int]] = []
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    que.append((y, x, 1, None, True, 0))
        # has_visited = set()
        change_direction_map = {
            (1,1) : (1, -1),
            (1,-1) : (-1, -1),
            (-1, 1) : (1,1),
            (-1,-1) : (-1, 1),
        }
        max_len = 0
        while que:
            y, x, length, last_d, can_change_direction, visited = que.pop(0)
            if visited & status(y, x):
                continue
            new_visited = visited | status(y, x)
            max_len = max(max_len, length)
            this_value: int = grid[y][x]
            # if (y,x, last_d) in has_visited:
            #     continue
            # has_visited.add((y,x, last_d))
            next_value_should_be = {
                1: 2,
                2: 0,
                0: 2,
            }[this_value]
            for dy, dx in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                next_y, next_x = y+dy, x+dx
                if next_y in [-1, rows] or next_x in [-1, cols]:
                    continue
                if grid[next_y][next_x] == next_value_should_be:
                    if last_d:
                        if (dy,dx) == last_d:
                            que.append((next_y, next_x, length+1, (dy,dx), can_change_direction, new_visited))
                        elif can_change_direction:
                            if (dy,dx) == change_direction_map[last_d]:
                                que.append((next_y, next_x, length+1, (dy,dx), False, new_visited))
                    else:
                        que.append((next_y, next_x, length+1, (dy,dx), can_change_direction, new_visited))

        return max_len

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int, can_turn: bool, target: int) -> int:
            i += DIRS[k][0]
            j += DIRS[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != target:
                return 0
            res = dfs(i, j, k, can_turn, 2 - target) + 1  # 直行
            if can_turn:
                res = max(res, dfs(i, j, (k + 1) % 4, False, 2 - target) + 1)  # 右转
            return res

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    for k in range(4):
                        ans = max(ans, dfs(i, j, k, True, 2) + 1)
        return ans

# @lc code=end

# print(Solution().lenOfVDiagonal(grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]))
print(Solution().lenOfVDiagonal(grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]))
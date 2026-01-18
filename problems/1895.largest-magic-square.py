#
# @lc app=leetcode id=1895 lang=python3
#
# [1895] Largest Magic Square
#

# @lc code=start
from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def is_magic_square(
                y: int,
                x: int,
                size: int
        ) -> bool :
            target_sum = sum(grid[y][_x] for _x in range(x,x+size))
            for _y in range(y, y+size):
                row_sum = 0
                for _x in range(x, x+size):
                    row_sum += grid[_y][_x]
                if target_sum != row_sum:
                    return False
            for _x in range(x, x+size):
                col_sum = 0
                for _y in range(y, y+size):
                    col_sum += grid[_y][_x]
                if target_sum != row_sum:
                    return False
            lt2rd = 0
            for d in range(size):
                _y, _x = y+d, x+d
                lt2rd += grid[_y][_x]
            if lt2rd != target_sum:
                return False
            ld2rt = 0
            for d in range(size):
                _y, _x = y+size-1-d, x+d
                ld2rt += grid[_y][_x]
            if ld2rt != target_sum:
                return False
            return True
        n, m = len(grid), len(grid[0])
        max_size = 0
        for y in range(n):
            for x in range(m):
                for size in range(1, min(n-y, m-x)+1):
                    if is_magic_square(y, x, size):
                        max_size = max(max_size, size)
                    
        return max_size


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sum = [[0] * (n + 1) for _ in range(m)]       # → 前缀和
        col_sum = [[0] * n for _ in range(m + 1)]         # ↓ 前缀和
        diag_sum = [[0] * (n + 1) for _ in range(m + 1)]  # ↘ 前缀和
        anti_sum = [[0] * (n + 1) for _ in range(m + 1)]  # ↙ 前缀和

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                row_sum[i][j + 1] = row_sum[i][j] + x
                col_sum[i + 1][j] = col_sum[i][j] + x
                diag_sum[i + 1][j + 1] = diag_sum[i][j] + x
                anti_sum[i + 1][j] = anti_sum[i][j + 1] + x

        # k×k 子矩阵的左上角为 (i−k, j−k)，右下角为 (i−1, j−1)
        for k in range(min(m, n), 0, -1):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    # 子矩阵主对角线的和
                    s = diag_sum[i][j] - diag_sum[i - k][j - k]

                    # 子矩阵反对角线的和等于 s
                    # 子矩阵每行的和都等于 s
                    # 子矩阵每列的和都等于 s
                    if anti_sum[i][j - k] - anti_sum[i - k][j] == s and \
                       all(row_sum[r][j] - row_sum[r][j - k] == s for r in range(i - k, i)) and \
                       all(col_sum[i][c] - col_sum[i - k][c] == s for c in range(j - k, j)):
                        return k

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/largest-magic-square/solutions/825422/go-qian-zhui-he-by-endlesscheng-59wj/

# @lc code=end

if __name__ == "__main__":
    print(Solution().largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
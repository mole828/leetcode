#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
from typing import List



class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        # 返回左上角在 (r1, c1)，右下角在 (r2, c2) 的子矩阵元素和
        def query(r1: int, c1: int, r2: int, c2: int) -> int:
            """
            二维前缀和，通过 0,0 到四个位置的方法，计算指定面积的和
            """
            return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]

        ans = 0
        for i in range(m):
            for j in range(n):
                # 边长为 ans+1 的正方形，左上角在 (i, j)，右下角在 (i+ans, j+ans)
                while i + ans < m and j + ans < n and query(i, j, i + ans, j + ans) <= threshold:
                    ans += 1
        return ans
        
# @lc code=end


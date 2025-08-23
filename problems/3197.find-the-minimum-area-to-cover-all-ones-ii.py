#
# @lc app=leetcode id=3197 lang=python3
# @lcpr version=30204
#
# [3197] Find the Minimum Area to Cover All Ones II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # [1,0,1]  [1, 2,  4 ]
        # [1,1,1]  [8, 16, 32]
        def status_of_place(i: int, j: int) -> int:
            return 1 << (i * cols + j)

        status_need = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    status_need |= status_of_place(i, j)
        print(status_need) # 32+16+8+4+1 = 61

        # left, right in [0, cols)
        # top, bottom in [0, rows)
        def status(left: int, right: int, top: int, bottom: int) -> int:
            _s = 0
            for i in range(top, bottom+1):
                for j in range(left, right+1):
                    _s |= status_of_place(i, j)
            # print((left, right, top, bottom), _s)
            return _s
        
        def iter_status():
            for left in range(cols):
                for right in range(left, cols):
                    for top in range(rows):
                        for bottom in range(top, rows):
                            yield status(left, right, top, bottom)
        
        min_area = float('inf')
        for i in iter_status():
            for j in iter_status():
                for k in iter_status():
                    if not (i & j or i & k or j & k):
                        if (i | j | k) & status_need == status_need:
                            min_area = min(min_area, i.bit_count() + j.bit_count() + k.bit_count())

        return min_area
    

# 把矩阵 a 顺时针旋转 90°
def rotate(a: List[List[int]]) -> List[List[int]]:
    return list(zip(*reversed(a)))

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.solve(grid), self.solve(rotate(grid)))

    def solve(self, a: List[List[int]]) -> int:
        # 3195. 包含所有 1 的最小矩形面积 I
        # 限定在 a 的 [l,r) 列中
        def minimumArea(a: List[List[int]], l: int, r: int) -> int:
            left = top = float('inf')
            right = bottom = 0
            for i, row in enumerate(a):
                for j, x in enumerate(row[l:r]):
                    if x:
                        left = min(left, j)
                        right = max(right, j)
                        top = min(top, i)
                        bottom = i
            return (right - left + 1) * (bottom - top + 1)

        ans = float('inf')
        m, n = len(a), len(a[0])

        if m >= 3:
            for i in range(1, m):
                for j in range(i + 1, m):
                    # 图片上左
                    area = minimumArea(a[:i], 0, n)
                    area += minimumArea(a[i:j], 0, n)
                    area += minimumArea(a[j:], 0, n)
                    ans = min(ans, area)

        if m >= 2 and n >= 2:
            for i in range(1, m):
                for j in range(1, n):
                    # 图片上中
                    area = minimumArea(a[:i], 0, n)
                    area += minimumArea(a[i:], 0, j)
                    area += minimumArea(a[i:], j, n)
                    ans = min(ans, area)

                    # 图片上右
                    area = minimumArea(a[:i], 0, j)
                    area += minimumArea(a[:i], j, n)
                    area += minimumArea(a[i:], 0, n)
                    ans = min(ans, area)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii/solutions/2819357/mei-ju-pythonjavacgo-by-endlesscheng-uu5p/
# @lc code=end

# print(Solution().minimumSum([[1,0,1],[1,1,1]]))
print(Solution().minimumSum([[0,0,1],[0,0,0],[0,0,0],[1,0,1]]))

#
# @lcpr case=start
# [[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1,0],[0,1,0,1]]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#

# @lc code=start
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for top in range(m):  # 枚举上边界
            a = [0] * n
            for bottom in range(top, m):  # 枚举下边界
                h = bottom - top + 1  # 高
                # 2348. 全 h 子数组的数目
                last = -1
                for j in range(n):
                    a[j] += mat[bottom][j]  # 把 bottom 这一行的值加到 a 中
                    if a[j] != h:
                        last = j  # 记录上一个非 h 元素的位置
                    else:
                        ans += j - last
        return ans
# @lc code=end

print(Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]]))

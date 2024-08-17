#
# @lc app=leetcode id=1937 lang=python3
# @lcpr version=
#
# [1937] Maximum Number of Points with Cost
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# Time Limit Exceeded, 141/157 cases passed (N/A)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for row in range(1, len(points)):
            row_a = points[row-1]
            row_b = points[row]
            for col in range(len(row_b)):
                row_b[col] += max(row_a[x]-abs(x-col) for x in range(len(row_a)))
        return max(points[-1])
    
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = [0] * n
        for i in range(m):
            g = [0] * n
            best = float("-inf")
            # 正序遍历
            for j in range(n):
                best = max(best, f[j] + j)
                g[j] = max(g[j], best + points[i][j] - j)
            
            best = float("-inf")
            # 倒序遍历
            for j in range(n - 1, -1, -1):
                best = max(best, f[j] - j)
                g[j] = max(g[j], best + points[i][j] + j)
            
            f = g
        
        return max(f)

# @lc code=end

print(Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))

#
# @lcpr case=start
# [[1,2,3],[1,5,1],[3,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[2,3],[4,2]]\n
# @lcpr case=end

#


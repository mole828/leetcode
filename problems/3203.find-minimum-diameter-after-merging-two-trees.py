#
# @lc app=leetcode id=3203 lang=python3
# @lcpr version=
#
# [3203] Find Minimum Diameter After Merging Two Trees
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


# Wrong Answer, 531/723 cases passed (N/A)
# [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]]
# 忽略了单个树高于这一答案的情况
class Solution:
    def floyd(edges: List[List[int]]) -> List[List[int]]:
        n = len(edges) + 1
        mat = [[float('inf')] * (n) for _ in range(n)]
        for i in range(n):
            mat[i][i] = 0
        for u, v in edges:
            mat[u][v] = 1
            mat[v][u] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        return mat

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        mat1 = Solution.floyd(edges1)
        mat2 = Solution.floyd(edges2)
        max1 = [max(row) for row in mat1]
        max2 = [max(row) for row in mat2]
        print(max1, max2)
        return min(max1) + min(max2) + 1
        

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/solutions/2826587/lian-jie-zhi-jing-zhong-dian-pythonjavac-0e1c/
class Solution:
    def diameter(self, edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        res = 0
        def dfs(x: int, fa: int) -> int:
            nonlocal res
            max_len = 0
            for y in g[x]:
                if y != fa:
                    sub_len = dfs(y, x) + 1
                    res = max(res, max_len + sub_len)
                    max_len = max(max_len, sub_len)
            return max_len
        dfs(0, -1)
        return res

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.diameter(edges1)
        d2 = self.diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


        
# @lc code=end

print(Solution().minimumDiameterAfterMerge([[0,1],[0,2],[0,3]], [[0,1]]))
print(Solution().minimumDiameterAfterMerge([[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]))
print(Solution().minimumDiameterAfterMerge([[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]],[[0,1],[0,2],[0,3]]))

#
# @lcpr case=start
# [[0,1],[0,2],[0,3]]\n[[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]\n[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]\n
# @lcpr case=end

#


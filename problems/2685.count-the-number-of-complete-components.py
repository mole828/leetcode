#
# @lc app=leetcode id=2685 lang=python3
# @lcpr version=30204
#
# [2685] Count the Number of Complete Components
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import numpy

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 初始化邻接矩阵
        mat = numpy.full((n, n), numpy.inf)
        numpy.fill_diagonal(mat, 0)  # 自己到自己的距离为0
        
        # 填充直接相连的边
        for i, j in edges:
            mat[i][j] = 1
            mat[j][i] = 1
        
        # Floyd-Warshall算法更新最短路径
        for k in range(n):
            mat = numpy.minimum(mat, mat[:, k, None] + mat[k, :])
        
        print(mat)

        # 寻找连通组件
        visited = [False] * n
        components = []
        for i in range(n):
            if not visited[i]:
                # 获取当前节点的可达节点
                reachable = (mat[i] < numpy.inf)
                component = numpy.where(reachable)[0].tolist()
                components.append(component)
                # 标记所有可达节点为已访问
                for node in component:
                    visited[node] = True
        print(components)

        # 统计完全组件数量
        count = 0
        for comp in components:
            k = len(comp)
            if k == 0:
                continue
            
            # 单节点情况
            if k == 1:
                count += 1
                continue
            
            # 多节点情况：检查所有非对角元素是否为1
            submatrix = mat[comp][:, comp]
            mask = ~numpy.eye(k, dtype=bool)  # 排除对角线
            if numpy.all(submatrix[mask] == 1):
                count += 1
        
        return count


        
# @lc code=end

print(Solution().countCompleteComponents(n=6, edges=[[0,1],[0,2],[1,2],[3,4]]))
print(Solution().countCompleteComponents(n=6, edges=[[0,1],[0,2],[1,2],[3,4],[3,5]]))

#
# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4],[3,5]]\n
# @lcpr case=end

#


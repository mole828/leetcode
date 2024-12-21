#
# @lc app=leetcode id=2872 lang=python3
# @lcpr version=30204
#
# [2872] Maximum Number of K-Divisible Components
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# Memory Limit Exceeded, 721/736 cases passed (N/A)
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        class Node:
            def __init__(self, id: int, value: int):
                self.id = id
                self.value = value
                self.children = []
                self.parent = None
                self.sum_with_children = 0
        nodes = [Node(id, value) for id, value in enumerate(values)]
        mat = [[0] * n for _ in range(n)]
        for edge in edges:
            mat[edge[0]][edge[1]] = 1
            mat[edge[1]][edge[0]] = 1
        root = nodes[0]
        
        visited = [False] * n
        def build_tree(node: Node, parent: Node):
            visited[node.id] = True
            for i, v in enumerate(mat[node.id]):
                if v == 1 and not visited[i]:
                    child = nodes[i]
                    node.children.append(child)
                    child.parent = node
                    build_tree(child, node)
        def init_sum_with_children(node: Node):
            node.sum_with_children = node.value
            for child in node.children:
                node.sum_with_children += init_sum_with_children(child)
            return node.sum_with_children

        build_tree(root, None)
        init_sum_with_children(root)
        # print([(node.id, node.sum_with_children) for node in nodes])
        def dfs(node: Node) -> int:
            count = 0
            if node.sum_with_children % k == 0:
                count += 1
            for child in node.children:
                count += dfs(child)
            return count
        return dfs(root)

# Memory Limit Exceeded, 719/736 cases passed (N/A)
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        mat = [[0] * n for _ in range(n)]
        for edge in edges:
            mat[edge[0]][edge[1]] = 1
            mat[edge[1]][edge[0]] = 1
        visited = [False] * n
        count = [0]
        def dfs(node: int):
            visited[node] = True
            sum_with_children = values[node]
            for i, v in enumerate(mat[node]):
                if v == 1 and not visited[i]:
                    sum_with_children += dfs(i)
            if sum_with_children % k == 0:
                count[0] += 1
            return sum_with_children
        dfs(0)
        return count[0]
        
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        def dfs(cur: int,fa: int) -> tuple:
            cnt = 0
            sm = values[cur]
            for nxt in g[cur]:
                if nxt == fa: continue
                nxt_cnt,nxt_sm = dfs(nxt,cur)
                cnt += nxt_cnt
                sm += nxt_sm
            if sm % k == 0:
                return (cnt + 1,0)
            return cnt,sm
        return dfs(0,-1)[0]


# @lc code=end

print(Solution().maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6))

#
# @lcpr case=start
# 5\n[[0,2],[1,2],[1,3],[2,4]]\n[1,8,1,4,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]\n[3,0,6,1,5,2,1]\n3\n
# @lcpr case=end

#


#
# @lc app=leetcode id=3372 lang=python3
#
# [3372] Maximize the Number of Target Nodes After Connecting Trees I
#

# @lc code=start
from collections import defaultdict
from functools import cache
from typing import Callable, List


NodeValue = tuple[int,int]
class Solution0:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        link: dict[NodeValue, set[NodeValue]] = defaultdict(set)
        for a,b in edges1:
            link[(1,a)].add((1,b))
            link[(1,b)].add((1,a))
        for a,b in edges2:
            link[(2,a)].add((2,b))
            link[(2,b)].add((2,a))
        nodes1 = sorted(key for key in link.keys() if key[0] == 1)
        nodes2 = sorted(key for key in link.keys() if key[0] == 2)
        nodes = sorted(key for key in link.keys())
        nodes_index = {v:i for i,v in enumerate(nodes)}
        # def bit_map(node_value: NodeValue) -> int:
        #     return 1<<nodes_index[node_value]
        res: list[int] = []
        for node1 in nodes1:
            _max = 0
            for node2 in nodes2:
                @cache
                def dfs(place: int, last_step: int) -> set[NodeValue]:
                    node_value = nodes[place]
                    dfs_result: set[NodeValue] = set([node_value])
                    if last_step == 0:
                        return dfs_result
                    next_nodes = link[node_value]
                    for next_node in next_nodes:
                        dfs_result |= dfs(nodes_index[next_node], last_step-1)
                    if node_value == node1:
                        dfs_result |= dfs(nodes_index[node2], last_step-1)
                    return dfs_result
                s = dfs(nodes_index[node1], k)
                _max = max(_max, len(s))
            res.append(_max)
        return res

class Solution:
    def buildTree(self, edges: List[List[int]], k: int) -> Callable[[int, int, int], int]:
        g: List[List[int]] = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int, d: int) -> int:
            if d > k:
                return 0
            cnt = 1
            for y in g[x]:
                if y != fa:
                    cnt += dfs(y, x, d + 1)
            return cnt
        return dfs

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        max2 = 0
        if k:
            dfs = self.buildTree(edges2, k - 1)
            max2 = max(dfs(i, -1, 0) for i in range(len(edges2) + 1))

        dfs = self.buildTree(edges1, k)
        return [dfs(i, -1, 0) + max2 for i in range(len(edges1) + 1)]

# @lc code=end

print(Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))
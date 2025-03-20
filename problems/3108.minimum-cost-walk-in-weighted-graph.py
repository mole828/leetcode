#
# @lc app=leetcode id=3108 lang=python3
#
# [3108] Minimum Cost Walk in Weighted Graph
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    # edge: list of (node0, node1, weight)
    # query: list of (node0, node1)
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        node_map: dict[int, dict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
        for a, b, w in edges:
            node_map[a][b].add(w)
            node_map[b][a].add(w)

        blocks: list[set[int]] = []
        has_meet = set()
        for i in range(n):
            if i in has_meet:
                continue
            block = set([i])
            que = deque([i])
            has_meet.add(i)
            while que:
                a = que.popleft()
                for b in node_map[a]:
                    if b not in block:
                        block.add(b)
                        que.append(b)
                        has_meet.add(b)
            blocks.append(block)

        block_index: dict[int, int] = {}
        for i, block in enumerate(blocks):
            for j in block:
                block_index[j] = i
        
        block_all_edges: list[list[int]] = [[] for _ in range(len(blocks))]
        for a,b,w in edges:
            block_all_edges[block_index[a]].append(w)
        
        block_all_edges_and = []
        for block in block_all_edges:
            and_ = -1
            for w in block:
                and_ &= w
            block_all_edges_and.append(and_)

        ans = []
        for a, b in query:
            if block_index[a] != block_index[b]:
                ans.append(-1)
                continue
            ans.append(block_all_edges_and[block_index[a]])
            
        return ans
        
# @lc code=end

print(Solution().minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(Solution().minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]))
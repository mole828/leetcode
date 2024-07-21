#
# @lc app=leetcode id=2392 lang=python3
# @lcpr version=
#
# [2392] Build a Matrix With Conditions
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict, deque
from typing import List

# TODO learn Topological Sorting
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(k)] for _ in range(k)]
        

        row_graph, col_graph = defaultdict(set), defaultdict(set)
        row_indegrees, col_indegrees = defaultdict(int), defaultdict(int)
        for i, j in rowConditions:
            if j not in row_graph[i]:
                row_graph[i].add(j)
                row_indegrees[j] += 1
        for i, j in colConditions:
            if j not in col_graph[i]:
                col_graph[i].add(j)
                col_indegrees[j] += 1
        
        row_queue, col_queue = deque(), deque()
        row_order, col_order = {}, {}
        row_order_counter, col_order_counter = 0, 0
        row_visited, col_visited = set(), set()
        for i in range(1, k+1):
            if row_indegrees[i] == 0:
                row_queue.append(i)
                row_visited.add(i)
        while row_queue:
            cur = row_queue.popleft()
            row_order[cur] = row_order_counter
            row_order_counter += 1
            for nxt in row_graph[cur]:
                if nxt in row_visited:
                    continue
                row_indegrees[nxt] -= 1
                if row_indegrees[nxt] <= 0:
                    row_visited.add(nxt)
                    row_queue.append(nxt)
        
        for i in range(1, k+1):
            if col_indegrees[i] == 0:
                col_queue.append(i)
                col_visited.add(i)
        while col_queue:
            cur = col_queue.popleft()
            col_order[cur] = col_order_counter
            col_order_counter += 1
            for nxt in col_graph[cur]:
                if nxt in col_visited:
                    continue
                col_indegrees[nxt] -= 1
                if col_indegrees[nxt] <= 0:
                    col_visited.add(nxt)
                    col_queue.append(nxt)

        if not (len(row_order) == k and len(col_order) == k):
            return []
        
        for i in range(1, k+1):
            res[row_order[i]][col_order[i]] = i
        return res
# @lc code=end

print(Solution().buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))

#
# @lcpr case=start
# 3\n[[1,2],[3,2]]\n[[2,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[2,3],[3,1],[2,3]]\n[[2,1]]\n
# @lcpr case=end

#


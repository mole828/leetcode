#
# @lc app=leetcode id=2642 lang=python3
#
# [2642] Design Graph With Shortest Path Calculator
#

# @lc code=start
from collections import defaultdict
from functools import cache
import heapq
import math
from typing import List, Callable, Tuple

# Time Limit Exceeded
class Graph:
    Not_Exist: float = math.inf

    cost_matrix: List[List[int]]
    find_func: Callable[[int,int],int]

    def addEdge(self, edge: List[int]) -> None:
        from_num, to_num, cost = edge
        self.cost_matrix[from_num][to_num] = cost 

        @cache
        def find(this: int, target: int, mask: int = 0) -> int:
            # print(f"find{this, target, mask}, has: {bin(mask)}")
            if this == target:
                return 0
            this_mask = 1 << this
            if mask & this_mask:
                # round
                return Graph.Not_Exist
            new_mask = mask | this_mask
            re = min(
                [
                    self.cost_matrix[this][target]
                ]+
                [
                    Graph.Not_Exist
                    if self.cost_matrix[this][new_this] is Graph.Not_Exist 
                    else self.cost_matrix[this][new_this] + find(new_this, target, new_mask)
                    for new_this in range(len(self.cost_matrix))
                    if new_this != this
                ]
            )
            # print(f"find{this, target, mask}, re={re}")
            return re
        
        self.find_func = find 


    def __init__(self, n: int, edges: List[List[int]]):
        self.cost_matrix = [
            [Graph.Not_Exist] * n 
            for _ in range(n)
        ]
        for edge in edges:
            self.addEdge(edge)

    def shortestPath(self, node1: int, node2: int) -> int:
        # print(f"shortestPath({node1}, {node2})")
        cost = self.find_func(node1, node2)
        return -1 if cost is Graph.Not_Exist else cost


class Graph:
    map: dict[int, dict[int, int]]
    def __init__(self, n: int, edges: List[List[int]]):
        self.map = defaultdict(dict)
        for edge in edges:
            self.addEdge(edge)
        
    def addEdge(self, edge: List[int]) -> None:
        from_num, to_num, cost = edge
        self.map[from_num][to_num] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        heap:list[tuple[int, int]] = [(0, node1)]
        visited = set()
        while heap:
            cost, this = heapq.heappop(heap)
            if this in visited:
                continue
            visited.add(this)
            if this == node2:
                return cost
            if this in self.map:
                for next_node in self.map[this]:
                    next_cost = self.map[this][next_node] 
                    heapq.heappush(heap, (next_cost+cost,next_node))
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
# @lc code=end


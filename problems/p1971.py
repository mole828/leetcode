from collections import defaultdict, deque
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(set)
        for i in edges:
            paths[i[0]].add(i[1])
            paths[i[1]].add(i[0])
        vertex_from_source = {source}
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            if vertex == destination:
                return True
            vertex_from_source.add(vertex)
            for i in paths[vertex]:
                if i not in vertex_from_source:
                    queue.append(i)
        return False
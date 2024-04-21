#
# @lc app=leetcode id=1971 lang=python3
# @lcpr version=
#
# [1971] Find if Path Exists in Graph
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 16/30 cases passed
    def validPath(self, n: int, edges: List[tuple[int,int]], source: int, destination: int) -> bool:
        arrival:list[set[int]] = [set([i]) for i in range(n)]
        def link(a: int, b: int):
            has = set()
            que = [b]
            while que:
                other = que.pop()
                if other in has:
                    continue
                arrival[a].add(other)
                arrival[other].add(a)
                has.add(other)
                for i in arrival[other]:
                    que.append(i)
        for a,b in edges:
            link(a,b)
            link(b,a)
        # print(arrival[40])
        return destination in arrival[source]
    
    # Time Limit Exceeded, 12/30 cases passed
    def validPath(self, n: int, edges: List[tuple[int,int]], source: int, destination: int) -> bool:
        arrival:list[set[int]] = [set([i]) for i in range(n)]
        for a,b in edges:
            arrival[a].add(b)
            arrival[b].add(a)
        def route(passed: set[int], a: int, b: int) -> bool:
            # print(passed, a, b)
            if a in passed: return False
            if b in arrival[a]: return True
            return any(route(passed|set([a]),c,b) for c in arrival[a])
        return route(set(), source, destination)

    def validPath(self, n: int, edges: List[tuple[int,int]], source: int, destination: int) -> bool:
        graph:list[set[int]] = [set([i]) for i in range(n)]
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        def route(passed: set[int], a:int, b:int):
            if a == b:
                return True
            passed.add(a)
            for neighbor in graph[a]:
                if neighbor not in passed:
                    if route(passed, neighbor, b):
                        return True
            return False
        return route(set(), source, destination)
# @lc code=end

print(Solution().validPath(
    50,
    [[41,40],[9,32],[48,14],[6,44],[18,41],[41,1],[7,41],[38,41],[19,4],[16,41],[41,43],[41,22],[41,21],[9,0],[41,48],[32,36],[24,44],[39,41],[48,17],[49,15],[47,41],[19,31],[11,41],[41,23],[41,49],[45,44],[2,49],[13,41],[35,41],[30,0],[5,44],[8,0],[41,20],[41,28],[12,11],[12,41],[49,10],[19,0],[0,37],[34,41],[42,48],[27,41],[0,41],[19,44],[41,26],[41,29],[33,41],[49,46],[41,25],[3,41]],
    40, 
    3
))

#
# @lcpr case=start
# 3\n[[0,1],[1,2],[2,0]]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[3,5],[5,4],[4,3]]\n0\n5\n
# @lcpr case=end

#


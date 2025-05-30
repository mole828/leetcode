#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
from typing import List


class Solution0:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def f(i: int) -> List[int]:
            res = [i]
            next_i = edges[i]
            while next_i != -1:
                if next_i in res:
                    return res
                res.append(next_i)
                next_i = edges[next_i]
            return res
        path1 = f(node1)
        path2 = f(node2)
        print(path1, path2)
        a = (-1,-1)

        for i,v in enumerate(path1):
            if v in path2:
                a = (max(i,path2.index(v)),v)
                break
                # return i
        b = (-1,-1)
        for i,v in enumerate(path2):
            if v in path1:
                b = (max(i,path1.index(v)),v)
                break
        print(a,b)
        return min(a,b)[1]


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def calc_dis(x: int) -> List[int]:
            dis = [n] * n
            d = 0
            while x >= 0 and dis[x] == n:
                dis[x] = d
                d += 1
                x = edges[x]
            return dis

        dis1 = calc_dis(node1)
        dis2 = calc_dis(node2)

        min_dis, ans = n, -1
        for i, (d1, d2) in enumerate(zip(dis1, dis2)):
            d = max(d1, d2)
            if d < min_dis:
                min_dis, ans = d, i
        return ans

# @lc code=end

print(Solution().closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
from collections import Counter, defaultdict
import math
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points.sort()
        k_map = defaultdict(lambda: defaultdict(list))
        for i, (y, x) in enumerate(points):
            # y = k * x + b
            # k = (y - y2) / (x - x2)
            # b = y - k * x

            for j in range(i):
                y2, x2 = points[j]
                g = math.gcd(y - y2, x - x2)
                # k = (y - y2) / (x - x2) if x != x2 else float('inf')
                k = (y - y2) // g, (x - x2) // g
                b = y - k[0] * x // k[1] if k[1] != 0 else x
                k_map[k][b].append((i, j))
        for k in list(k_map.keys()):
            if len(k_map[k]) == 1:
                del k_map[k]
        # res = 0
        # for k in k_map:
        #     k_b_map = k_map[k]
        #     cnt = 0
        #     for b in k_b_map:
        #         pairs = k_b_map[b]
        #         res += cnt * len(pairs)
        #         cnt += len(pairs)
        # return res
        res_set = set()
        for k in k_map:
            pair0_list = []
            k_b_map = k_map[k]
            for b in k_b_map:
                pairs = k_b_map[b]
                for pair0 in pair0_list:
                    for pair1 in pairs:
                        res_set.add(tuple(sorted([pair0[0], pair0[1], pair1[0], pair1[1]])))
                pair0_list.extend(pairs)
            print(k, len(res_set))
        return len(res_set)
    
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(list) 
        groups2 = defaultdict(list) 

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else math.inf
                b = (y * dx - x * dy) / dx if dx else x
                groups[k].append(b)
                groups2[(x + x2, y + y2)].append(k)

        ans = 0
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans += s * c
                s += c

        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c 
                s += c

        return ans

        
# @lc code=end

# print(Solution().countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]]))
# print(Solution().countTrapezoids([[32,-8],[-78,-25],[72,-8],[-77,-25]]))
# print(Solution().countTrapezoids([[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]]))

print(Solution().countTrapezoids([[66,39],[46,30],[-52,-57],[66,-25],[66,-13],[-38,58],[54,-91],[-29,30],[66,-29],[35,20],[-60,-7],[-47,-10],[97,-91],[-93,75],[66,4],[-93,38],[87,-7],[65,38],[87,38],[79,76]]))
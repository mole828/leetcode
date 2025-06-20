#
# @lc app=leetcode id=3443 lang=python3
#
# [3443] Maximum Manhattan Distance After K Changes
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        d_map: dict[str, tuple[int, int]] = {
            'N': (0, 1),
            'W': (-1, 0),
            'E': (1, 0),
            'S': (0, -1),
        }
        max_distance = 0
        que = [(0, 0, -k, 0, 0)] # neg_distance, index, neg_k, y, x
        heapq.heapify(que)
        has_visited = set()
        while que:
            tup = heapq.heappop(que)
            if tup in has_visited:
                continue
            has_visited.add(tup)
            neg_distance, index, neg_k, y, x = tup
            max_distance = max(max_distance, -neg_distance)
            if index == len(s):
                continue
            old_d = d_map[s[index]]
            if neg_k < 0:
                for other_for in d_map.keys():
                    if other_for != s[index]:
                        new_y, new_x = y + d_map[other_for][0], x + d_map[other_for][1]
                        new_distance = abs(new_y) + abs(new_x)
                        heapq.heappush(que, (-new_distance, index + 1, neg_k + 1, new_y, new_x))
            new_y, new_x = y + old_d[0], x + old_d[1]
            new_distance = abs(new_y) + abs(new_x)
            heapq.heappush(que, (-new_distance, index + 1, neg_k, new_y, new_x))
            
        return max_distance

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def f(a: int, b: int, k: int) -> tuple[int,int]:
            big, small = max(a, b), min(a, b)
            if k >= small:
                return big + small, k - small
            else:
                # k < small
                return big - small + 2*k , 0

        count = defaultdict(int)
        max_distance = 0
        for c in s:
            count[c] += 1
            this_last_k = k
            dy, this_last_k = f(count['N'], count['S'], this_last_k)
            dx, this_last_k = f(count['E'], count['W'], this_last_k)
            max_distance = max(max_distance, dy+dx)
        return max_distance


# @lc code=end

print(Solution().maxDistance("NWSE", k=1))
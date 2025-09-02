#
# @lc app=leetcode id=3025 lang=python3
#
# [3025] Find the Number of Ways to Place People I
#

# @lc code=start
from collections import defaultdict
from typing import List

Point = tuple[int, int] # (x, y)
class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        for i in range(len(points)):
            points[i] = (points[i][0], points[i][1])
        def on_left_top(p1: Point, p2: Point) -> bool:
            return p1[0] <= p2[0] and p1[1] >= p2[1]
        def on_space(left_top: Point, right_bottom: Point, other: Point) -> bool:
            return left_top[0] <= other[0] <= right_bottom[0] and left_top[1] >= other[1] >= right_bottom[1]
        left_top_map: dict[Point, List[tuple[int, Point]]] = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                left_top = points[i]
                right_bottom = points[j]
                if on_left_top(left_top, right_bottom):
                    left_top_map[right_bottom].append(left_top)
        print(left_top_map)
        count = 0
        for right_bottom in left_top_map:
            for left_top in left_top_map[right_bottom]:
                for i in range(len(points)):
                    if points[i] == left_top or points[i] == right_bottom:
                        continue
                    if on_space(left_top, right_bottom, points[i]):
                        break
                else:
                    count += 1

        return count
# @lc code=end

print(Solution().numberOfPairs(points = [[6,2],[4,4],[2,6]]))
print(Solution().numberOfPairs(points = [[0,0],[0,3]]))

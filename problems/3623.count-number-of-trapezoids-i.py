#
# @lc app=leetcode id=3623 lang=python3
#
# [3623] Count Number of Trapezoids I
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List

MOD = 10**9 + 7
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        for y, x in points:
            lines[x].add(y)
        xs = sorted(lines.keys())
        res = 0
        for index_a in range(len(xs)):
            line_a = xs[index_a]
            set_a = lines[line_a]
            count_a = len(set_a)
            for index_b in range(index_a + 1, len(xs)):
                line_b = xs[index_b]
                set_b = lines[line_b]
                count_b = len(set_b)
                # print( line_a, line_b, set_a, set_b)
                res += count_a * (count_a - 1) // 2 * count_b * (count_b - 1) // 2
        return res % MOD

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = Counter(x for y,x in points)
        ans = 0
        left_pick_sum = 0
        for c in cnt.values():
            k = c * (c - 1) // 2
            ans += k * left_pick_sum
            left_pick_sum += k
        return ans % MOD

# @lc code=end

print(Solution().countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))
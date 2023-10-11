#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people_got = defaultdict(int)
        for begin,end in flowers:
            for i in range(begin, end+1):
                people_got[i] += 1
        return [people_got[i] for i in people]
    
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        def f(i: int):
            times = 0
            for begin, end in flowers:
                if begin<=i<=end:
                    times += 1
            return times
        return [f(i) for i in people]

from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(s for s,_ in flowers)
        ends = sorted(s for _,s in flowers)
        return [
            bisect_right(starts, p) - bisect_left(ends, p) 
            for p in people
        ]

# @lc code=end

print(Solution().fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
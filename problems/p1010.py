from collections import Counter
from typing import List
import math


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter([t%60 for t in time])
        ans = 0
        for v in [counter.pop(0,0),counter.pop(30,0)]:
            ans += int(v*(v-1)/2)
        while len(counter):
            k,v = counter.popitem()
            sub = counter.pop(60-k,0)
            ans += v*sub
        return ans
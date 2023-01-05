from collections import Counter
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def find(nums, x):
            count = Counter(nums)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[num] * count[(x - 1) ^ num] for num in count)
                count = Counter({num >> 1: count[num] + count[num ^ 1] for num in count})
                x >>= 1
            return res // 2
        return find(nums, high + 1) - find(nums, low)
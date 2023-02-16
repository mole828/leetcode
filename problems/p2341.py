from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [
            sum(x//2 for x in counter.values()), 
            sum(x%2 for x in counter.values())
        ]

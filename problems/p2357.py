from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(x for x in Counter(nums) if x!=0))
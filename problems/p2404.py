from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return sorted([[1, -1]] + [[-v, k] for k, v in Counter(nums).items() if not (k % 2)])[0][1]
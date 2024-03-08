from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        most_common = counter.most_common()
        count_need = most_common[0][1] 
        freq = 0
        for _,count in most_common:
            if count != count_need:
                break
            freq += count 
        return freq
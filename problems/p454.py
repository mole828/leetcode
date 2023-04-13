from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c0,c1 = [
            Counter([a+b for a in nums1 for b in nums2]),
            Counter([a+b for a in nums3 for b in nums4])
        ]
        ans = 0
        for x in c0:
            ans += c0[x]*c1[-x]
        return ans
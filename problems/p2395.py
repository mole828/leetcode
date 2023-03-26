from collections import defaultdict
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        a,b = nums[:2]
        m = defaultdict(int)
        m[a+b] += 1
        for i in range(2,len(nums)):
            a, b = b, nums[i]
            m[a+b] += 1
        return max(m.values())>1

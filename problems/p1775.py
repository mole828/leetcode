from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        d = abs(s1-s2)
        if d==0:return 0
        big, small = [nums1,nums2] if s1>s2 else [nums2,nums1]
        stepLengths = sorted([x-1 for x in big] + [6-x for x in small])
        step = 0
        while d:
            if not len(stepLengths):-1
            stepLength = stepLengths.pop(-1)
            if stepLength<=0:return -1
            d -= min(stepLength, d)
            step += 1
        return step
        

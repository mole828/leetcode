#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
import numpy

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = sum( [len(nums1), len(nums2)] )
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        take = 2 if n % 2 == 0 else 1
        seek = n // 2 - take + 1
        print(n,take,seek)
        while seek:
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
            seek-=1
            # print(nums1, nums2)
        mids = []
        while take:
            if nums1[0] < nums2[0]:
                mids.append(nums1.pop(0)) 
            else:
                mids.append(nums2.pop(0)) 
            take-=1
        return numpy.average(mids).__float__()
# @lc code=end


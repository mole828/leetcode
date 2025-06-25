#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        products = sorted([a*b for a in nums1 for b in nums2])
        return products[k-1]
        
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(p: int) -> int:
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    cnt += bisect_right(nums2, p / x)
                elif x < 0:
                    cnt += n - bisect_left(nums2, p / x)
                else:
                    cnt += n * int(p >= 0)
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))
        return bisect_left(range(-mx, mx + 1), k, key=count) - mx

# @lc code=end


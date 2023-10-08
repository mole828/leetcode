#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
from collections import defaultdict
from functools import cache
import pprint
from typing import List, TypeVar
from numpy import array, dtype
from numpy.typing import ArrayLike

class Solution:
    # def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    #     T = TypeVar("T")
    #     def sons(nums: List[T])->List[List[T]]:
    #         ans = []
    #         if nums:
    #             item = nums.pop(0)
    #             ss = sons(nums)
    #             for s in ss:
    #                 ans.append([item]+s)
    #                 ans.append(s)
    #             ans.append([item])
    #         return ans
    #     ls1:defaultdict[int,list[ArrayLike]] = defaultdict(list)
    #     ls2:defaultdict[int,list[ArrayLike]] = defaultdict(list)
    #     for son in sons(nums1):
    #         ls1[len(son)].append(array(son))
    #     for son in sons(nums2):
    #         ls2[len(son)].append(array(son))
    #     return max(sum(a*b) for l in ls1.keys() for a in ls1[l] for b in ls2[l])
    # def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    #     max_sum = [nums1[0] * nums2[0]]
    #     summary = [0]
    #     def dp(i1: int, i2: int):
    #         if i1 == len(nums1) or i2 == len(nums2):return
    #         a, b = nums1[i1], nums2[i2]
    #         summary[0] += a * b 
    #         max_sum[0] = max(summary[0], max_sum[0])
    #         dp(i1+1, i2+1)
    #         summary[0] -= a * b 
    #         dp(i1+1, i2)
    #         dp(i1, i2+1)
    #     dp(0,0)
    #     return max_sum[0]
    # def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    #     m, n = len(nums1), len(nums2)
        
    #     dp = array([[float('-inf')]*(n+1)]*(m+1), float)

    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             curr_product = nums1[i-1] * nums2[j-1]
    #             dp[i][j] = max(
    #                 dp[i][j],
    #                 curr_product,
    #                 dp[i-1][j],
    #                 dp[i][j-1],
    #                 curr_product + dp[i-1][j-1],
    #             )
    #     return int(dp[m][n])
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i1: int, i2: int) -> int:
            if i1 < 0 or i2 < 0: return float('-inf') 
            v = nums1[i1] * nums2[i2]
            return max(
                v, 
                dp(i1-1,i2),
                dp(i1,i2-1),
                dp(i1-1,i2-1) + v,
            ) 
        return dp(len(nums1)-1,len(nums2)-1)

# @lc code=end
print(Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))

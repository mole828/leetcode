#
# @lc app=leetcode id=3321 lang=python3
#
# [3321] Find X-Sum of All K-Long Subarrays II
#

# @lc code=start
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        large_part = SortedList()
        small_part = SortedList()
        cnt = defaultdict(int)
        x_sum = 0
        n = len(nums)
        def add(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if large_part and p > large_part[0]:
                nonlocal x_sum
                x_sum += p[0] * p[1]
                large_part.add(p)
            else:
                small_part.add(p)

        def remove(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if p in large_part:
                nonlocal x_sum
                x_sum -= p[0] * p[1]
                large_part.remove(p)
            else:
                small_part.remove(p)

        ans = [0] * (n - k + 1)
        for i, v in enumerate(nums):
            remove(v)
            cnt[v] += 1
            add(v)
            j = i - k + 1
            if j < 0:
                continue
            while small_part and len(large_part) < x:
                p = small_part.pop()
                large_part.add(p)
                x_sum += p[0] * p[1]
            while len(large_part) > x:
                p = large_part.pop(0)
                x_sum -= p[0] * p[1]
                small_part.add(p)
            ans[j] = x_sum

            remove(nums[j])
            cnt[nums[j]] -= 1
            add(nums[j])
        return ans
        
# @lc code=end

print(Solution().findXSum(nums=[1,1,2,2,3,4,2,3], k=6, x=2))
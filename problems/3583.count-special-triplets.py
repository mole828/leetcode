#
# @lc app=leetcode id=3583 lang=python3
#
# [3583] Count Special Triplets
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counter = defaultdict(list)
        n = len(nums)
        for i, num in enumerate(nums):
            counter[num].append(i)
        result = 0
        if 0 in counter:
            zero_count = len(counter[0])
            result += zero_count * (zero_count - 1) * (zero_count - 2) // 6
        for j in range(n):
            num_j = nums[j]
            if num_j == 0:
                continue
            double_num_j = num_j * 2
            if double_num_j in counter:
                p = bisect_left(counter[double_num_j], j)
                result += (len(counter[double_num_j]) - p) * p
        return result % (10**9 + 7)
            
        
# @lc code=end

print(Solution().specialTriplets([0,1,0,0]))
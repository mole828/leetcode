#
# @lc app=leetcode id=3350 lang=python3
#
# [3350] Adjacent Increasing Subarrays Detection II
#

# @lc code=start
from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        arr = []
        k_arr = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if arr:
                    k_arr.append(min(count, arr[-1]))
                arr.append(count)
                count = 1
        if arr:
            k_arr.append(min(count, arr[-1]))
        arr.append(count)
        print(arr, k_arr)
        ans_possible = []
        if arr:
            ans_possible.append(max(arr)//2)
        if k_arr:
            ans_possible.append(max(k_arr))
        return max(ans_possible)
# @lc code=end

# print(Solution().maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))  # 3
print(Solution().maxIncreasingSubarrays([1,2,3,4,4,4,4,4,5,6,7]))  # 3
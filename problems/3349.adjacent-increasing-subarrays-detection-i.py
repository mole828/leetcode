#
# @lc app=leetcode id=3349 lang=python3
#
# [3349] Adjacent Increasing Subarrays Detection I
#

# @lc code=start
from typing import List

def is_increasing(arr: List[int]) -> bool:
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for left in range(len(nums) - 2*k + 1):
            mid = left + k
            right = mid + k
            print(left, mid, right)
            print(nums[left:mid], nums[mid:right])
            if is_increasing(nums[left:mid]) and is_increasing(nums[mid:right]):
                return True
        return False
# @lc code=end

print(
    Solution().hasIncreasingSubarrays(
        nums = [2,5,7,8,9,2,3,4,3,1], k = 3
    )
)
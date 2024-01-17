#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right :
            mid = (right+left)//2
            vmid = nums[mid]
            vleft = nums[left]
            vright = nums[right]
            if vleft <= vmid <= vright:
                break
            if mid == right or mid == left:
                return vright
            if vleft > vmid < vright:
                right = mid
            if vleft < vmid > vright:
                left = mid
        return nums[left]


# @lc code=end

print(Solution().findMin([11,13,15,17]))
print(Solution().findMin([3,4,5,1,2]))
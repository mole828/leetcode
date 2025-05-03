#
# @lc app=leetcode id=33 lang=python3
# @lcpr version=30204
#
# [33] Search in Rotated Sorted Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = nums.index(min(nums))
        nums = nums[min_index:] + nums[:min_index]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return (mid + min_index) % len(nums)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


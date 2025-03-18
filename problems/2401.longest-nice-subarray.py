#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#

# @lc code=start
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, 0
        window_or = 0
        max_window_size = 0
        while right < n:
            new_number = nums[right]
            right += 1
            while window_or & new_number:
                pop_number = nums[left]
                left += 1
                window_or ^= pop_number
            window_or ^= new_number
            max_window_size = max(max_window_size, right - left)

        return max_window_size


# @lc code=end

print(Solution().longestNiceSubarray([1,3,8,48,10]))

print(Solution().longestNiceSubarray(
    [904163577,321202512,470948612,490925389,550193477,87742556,151890632,655280661,4,263168,32,573703555,886743681,937599702,120293650,725712231,257119393]
))
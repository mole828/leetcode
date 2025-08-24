#
# @lc app=leetcode id=1493 lang=python3
# @lcpr version=30204
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = [0,0]
        left = 0
        max_len = 0
        for right, num in enumerate(nums):
            window[num] += 1
            while window[0] > 1:
                window[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        
        return max_len

        
# @lc code=end



#
# @lcpr case=start
# [1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#


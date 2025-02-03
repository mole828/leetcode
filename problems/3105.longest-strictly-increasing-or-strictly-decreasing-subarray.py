#
# @lc app=leetcode id=3105 lang=python3
# @lcpr version=30204
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


# 理解错误，这里的递增和递减是指连续的递增和递减
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_stack = []
        decreasing_stack = []
        max_len = 0
        for x in nums:
            while increasing_stack and increasing_stack[-1] >= x:
                increasing_stack.pop()
            increasing_stack.append(x)
            while decreasing_stack and decreasing_stack[-1] <= x:
                decreasing_stack.pop()
            decreasing_stack.append(x)
            max_len = max(max_len, len(increasing_stack), len(decreasing_stack))
        return max_len
    

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incraesing = 1
        decreasing = 1
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incraesing += 1
                decreasing = 1
            elif nums[i] < nums[i-1]:
                decreasing += 1
                incraesing = 1
            else:
                incraesing = 1
                decreasing = 1
            max_len = max(max_len, incraesing, decreasing)
        return max_len
        
# @lc code=end

print(Solution().longestMonotonicSubarray([1,4,3,3,2]))  # 2

#
# @lcpr case=start
# [1,4,3,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1752 lang=python3
# @lcpr version=30204
#
# [1752] Check if Array Is Sorted and Rotated
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums + nums
        # 定义最大递增计数
        max_count = 0
        count = 0
        for i in range(1, len(arr)):
            if arr[i] >= arr[i-1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        else:
            max_count = max(max_count, count)
        return max_count >= len(nums) - 1
        
# @lc code=end

# print(Solution().check([3,4,5,1,2]))  # True
print(Solution().check([1,1,1]))

#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


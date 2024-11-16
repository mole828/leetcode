#
# @lc app=leetcode id=3254 lang=python3
# @lcpr version=30204
#
# [3254] Find the Power of K-Size Subarrays I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            arr = nums[i : i + k]
            is_ascending = all(arr[i] + 1 == arr[i + 1] for i in range(len(arr) - 1))
            if is_ascending:
                result.append(arr[-1])
            else:
                result.append(-1)
        return result
        
# @lc code=end

print(Solution().resultsArray([1,2,3,4,3,2,5], 3))

#
# @lcpr case=start
# [1,2,3,4,3,2,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,2,3,2]\n2\n
# @lcpr case=end

#


#
# @lc app=leetcode id=945 lang=python3
# @lcpr version=
#
# [945] Minimum Increment to Make Array Unique
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        has: set[int] = set()
        inc_times = 0
        for num in nums:
            while num in has:
                inc_times += 1
                num += 1
            has.add(num)
        return inc_times
    
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament


# @lc code=end

print(Solution().minIncrementForUnique([1,2,2]))

print(Solution().minIncrementForUnique([3,2,1,2,1,7]))

#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,2,1,7]\n
# @lcpr case=end

#


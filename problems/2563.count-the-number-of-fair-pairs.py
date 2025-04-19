#
# @lc app=leetcode id=2563 lang=python3
# @lcpr version=
#
# [2563] Count the Number of Fair Pairs
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List


# Time Limit Exceeded, 47 / 54 testcases passed
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if lower <= a + b <= upper:
                    print((i,j))
                    ans += 1
        return ans
    

# 2025-04-19
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            a = nums[i]
            l = lower - a
            r = upper - a
            j = bisect_left(nums, l, i+1)
            k = bisect_right(nums, r, i+1)
            ans += k - j
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,7,4,4,5]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,7,9,2,5]\n11\n11\n
# @lcpr case=end

#


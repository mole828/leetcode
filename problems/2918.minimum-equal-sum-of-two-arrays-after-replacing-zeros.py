#
# @lc app=leetcode id=2918 lang=python3
# @lcpr version=30204
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def prepare(nums: List[int]) -> tuple[int, int]:
            sum_ = 0
            zero_count = 0
            for num in nums:
                if num == 0:
                    zero_count += 1
                else:
                    sum_ += num
            return sum_, zero_count
        sum1, zero_count1 = prepare(nums1)
        sum2, zero_count2 = prepare(nums2)
        print(sum1, zero_count1)
        print(sum2, zero_count2)
        if zero_count1 == 0 and zero_count2 == 0:
            if sum1 == sum2:
                return sum1
            return -1
        if zero_count1 == 0:
            if sum2 + zero_count2 > sum1:
                return -1
            return sum1
        if zero_count2 == 0:
            if sum1 + zero_count1 > sum2:
                return -1
            return sum2
        return max(sum1 + zero_count1, sum2 + zero_count2)
        
# @lc code=end

print(Solution().minSum([17,1,13,12,3,13], [2,25]))

#
# @lcpr case=start
# [3,2,0,1,0]\n[6,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,2,0]\n[1,4]\n
# @lcpr case=end

#


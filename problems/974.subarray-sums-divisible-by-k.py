#
# @lc app=leetcode id=974 lang=python3
# @lcpr version=
#
# [974] Subarray Sums Divisible by K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        for left in range(len(nums)):
            for right in range(left,len(nums)):
                sub = nums[left:right+1]
                sub_sum = sum(sub)
                if sub_sum % k == 0:
                    count += 1
        return count
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        for left in range(len(nums)):
            sub_sum = 0
            for right in range(left,len(nums)):
                sub_sum += nums[right]
                if sub_sum % k == 0:
                    count += 1
        return count
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map = {0:[-1]}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem in map:
                count += len(map[rem])
                map[rem].append(i)
            else:
                map[rem] = [i]
        return count
# @lc code=end



#
# @lcpr case=start
# [4,5,0,-2,-3,1]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n9\n
# @lcpr case=end

#


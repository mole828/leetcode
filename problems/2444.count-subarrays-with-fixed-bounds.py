#
# @lc app=leetcode id=2444 lang=python3
# @lcpr version=
#
# [2444] Count Subarrays With Fixed Bounds
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 34/52 cases passed
    def _countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                sub = nums[left:right+1]
                if min(sub)==minK and max(sub)==maxK:
                    count += 1
        return count 
    # Time Limit Exceeded, 45/52 cases passed
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        new_nums:list[list[int]] = [] 
        last = 0
        for i,num in enumerate(nums):
            if minK<=num<=maxK:
                continue
            sub = nums[last:i]
            new_nums.append(sub)
            # print(sub)
            last = i+1
        new_nums.append(nums[last:])
        return sum(self._countSubarrays(ns,minK,maxK) for ns in new_nums)
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0 
        left = -1 
        maxI = -1
        minI = -1
        for i,num in enumerate(nums):
            if not minK<=num<=maxK:
                left = i
            if num==minK:
                minI = i 
            if num==maxK:
                maxI = i 
            count += max(0, min(maxI,minI)-left)
        return count
# @lc code=end

print(Solution().countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))

#
# @lcpr case=start
# [1,3,5,2,7,5]\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n1\n1\n
# @lcpr case=end

#


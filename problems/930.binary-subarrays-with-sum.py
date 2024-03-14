#
# @lc app=leetcode id=930 lang=python3
# @lcpr version=
#
# [930] Binary Subarrays With Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# Time Limit Exceeded
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        for l in range(1,len(nums)+1):
            for left in range(len(nums)-l+1):
                right = left + l 
                sub = nums[left:right] 
                if sum(sub) == goal:
                    count += 1
        return count
    

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        reduce = [0] * (len(nums)+1)
        reduce[0] += 1
        summary = 0
        for num in nums:
            summary += num 
            reduce[summary] += 1
        print(reduce)
        if goal == 0:
            return sum(int((x-1)*x/2) for x in reduce)
        return sum(reduce[i]*reduce[i+goal] for i in range(len(reduce)-goal))



# @lc code=end

print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
print(Solution().numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))
print(Solution().numSubarraysWithSum(nums = [1,1,1,1,1], goal = 5))

#
# @lcpr case=start
# [1,0,1,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n0\n
# @lcpr case=end

#


#
# @lc app=leetcode id=525 lang=python3
# @lcpr version=
#
# [525] Contiguous Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)+1):
                sub = nums[left:right]
                if sub.count(0) == sub.count(1):
                    maxLength = max(maxLength, len(sub))
        return maxLength
    
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index:dict[int, list[int]] = defaultdict(list)
        summary = 0
        index[0].append(-1)
        for i,num in enumerate(nums):
            summary += 1 if num else -1 
            index[summary].append(i)
        maxLength = 0
        for key in index:
            arr = index[key]
            if len(arr) > 1:
                maxLength = max(arr[-1]-arr[0],maxLength)
        return maxLength
# @lc code=end



#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

#


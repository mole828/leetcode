#
# @lc app=leetcode id=1574 lang=python3
# @lcpr version=
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List
import numpy as np


# 理解错误 Wrong Answer
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        @cache
        def dp(i: int, v: int) -> int:
            if i == len(arr):
                return 0
            a = (dp(i+1, arr[i])) if arr[i] >= v else np.inf
            b = dp(i+1, v) + 1
            print((i,v), min(a,b))
            return min(a,b)
        return dp(0, -1)
    
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0
        ans = right
        left = 0
        while True:
            while right == n or arr[left] <= arr[right]:
                ans = min(ans, right - left - 1) 
                if arr[left] > arr[left + 1]:
                    return ans
                left += 1
            right += 1

# @lc code=end

print(Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))

#
# @lcpr case=start
# [1,2,3,10,4,2,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


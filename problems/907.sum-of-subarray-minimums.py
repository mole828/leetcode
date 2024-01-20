#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
from typing import List

# Time Limit Exceeded
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        length = len(arr)
        minSum = 0
        for left in range(length):
            minNum = arr[left]
            for right in range(left, length):
                minNum = min(minNum, arr[right])
                minSum += minNum
        return minSum % (10**9 + 7)
    
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result 
# @lc code=end

print(Solution().sumSubarrayMins([3,1,2,4]))
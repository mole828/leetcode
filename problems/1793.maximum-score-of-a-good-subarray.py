#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
from functools import cache
from typing import List

from sortedcontainers import SortedList

# wrong
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # min value matrix
        matrix = [[float('inf')] * len(nums) for _ in range(len(nums))]
        for i,num in enumerate(nums):
            for y in range(len(nums)):
                for x in range( max(0,i-y), min(len(nums), i+y+1) ):
                    matrix[y][x] = min(num, matrix[y][x])
        result = 0
        for length,line in enumerate(matrix, start=1):
            line_max = length*max(line[
                max(0, k-length): min(len(matrix),k+length)
            ])
            print(line, length, line_max)
            result = max(result, line_max)
        return result

# wrong
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        @cache
        def f(x: int, y: int)->int:
            if y==0: return nums[x]
            return min(
                f(
                    min(max(0, x+dx),len(nums)-1),
                    y-1,
                ) for dx in [0,1]
            )
        return max(
            f(x,y)*(y+1) 
            for y in range(len(nums)) 
            for x in range(
                max(0, k-y),
                min(k+y+1, len(nums)-y)
            ) 
        )
                
            
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res=nums[k]
        i=k
        j=k
        min_val=nums[k]

        while i>0 or j<len(nums)-1:
            if i==0:
                j+=1
                min_val=min(min_val,nums[j])
            elif j==len(nums)-1:
                i-=1
                min_val=min(min_val,nums[i])
            elif nums[i-1]>nums[j+1]:
                i-=1
                min_val=min(min_val,nums[i])
            else:
                j+=1
                min_val=min(min_val,nums[j])
            res=max(res,min_val*(j-i+1))
            print(nums[i:j], res)
        return res
        


# @lc code=end
print(Solution().maximumScore(nums = [1,4,3,7,4,5], k = 3))
print(Solution().maximumScore(nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872], k = 5))
print(Solution().maximumScore(nums = [8182,1273,9847,6230,52,1467,6062,726,4852,4507,2460,2041,500,1025,5524], k = 8))


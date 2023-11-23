#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
from typing import List

def isArithmetic(arr: List[int])->bool:
    if len(arr)>1:
        d = arr[1] - arr[0] 
        for i in range(1,len(arr)):
            dd = arr[i] - arr[i-1]
            if dd != d:
                return False
    return True

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for a,b in zip(l,r):
            # print(a,b)
            # print(nums[a:b+1])
            arr = sorted(nums[a:b+1])
            output.append(isArithmetic(arr))
        return output

# @lc code=end

print(Solution().checkArithmeticSubarrays(
    nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
))

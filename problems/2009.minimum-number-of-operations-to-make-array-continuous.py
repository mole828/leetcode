#
# @lc app=leetcode id=2009 lang=python3
#
# [2009] Minimum Number of Operations to Make Array Continuous
#

# @lc code=start
from bisect import bisect_right
from collections import Counter
from functools import cache
from typing import List


# 全匹配 时间复杂度过高
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        has_sorted = sorted(nums)
        @cache 
        def begin2end(begin: int, end: int):
            return sum((count - Counter(num for num in range(begin,end))).values())
        @cache
        def beginWith(begin: int) -> int:
            return begin2end(begin, begin + n)
        return min(
            beginWith(begin) for begin in has_sorted
        )

# 滑动窗口 二分查找右边界 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        result = float('inf')
        
        for i, num in enumerate(nums):
            idx = bisect_right(nums, num + n -1)
            length = idx - i
            ops = n - length
            result = min(result, ops)
            
        return result

# 滑动窗口 维护实际窗口
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        left, right = 1, n 
        # print(left, right)
        ir = bisect_right(nums, right)
        centerNums = nums[:ir]
        leftNums = nums[ir:]
        # print(centerNums, leftNums)
        result = len(centerNums)
        while leftNums:
            num = leftNums.pop(0)
            left, right = num-n+1, num
            centerNums.append(num) 
            while centerNums and centerNums[0] < left:
                centerNums.pop(0)
            result = max(result, len(centerNums)) 
            # print(centerNums, leftNums, result)
        return n - result
# @lc code=end

print(Solution().minOperations([4,2,5,3]))
print(Solution().minOperations([8,5,9,9,8,4]))
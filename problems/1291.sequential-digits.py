#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
import bisect
from typing import List


def digits():
    arr = []
    for i in range(1,10):
        for j in range(i+1, 10):
            word = ''.join(str(c) for c in range(i,j+1))
            arr.append(int(word))
    arr.sort()
    return arr 

nums = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return nums[bisect.bisect_left(nums,low): bisect.bisect_right(nums,high)]
# @lc code=end

print(digits())
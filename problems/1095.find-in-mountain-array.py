#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
from functools import cache
from typing import Callable, Union


class MountainArray:
   _MountainArray__secret: list[int]
   def get(self, index: int) -> int:
       return self._MountainArray__secret[index]
   def length(self) -> int:
       return len(self._MountainArray__secret)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr:list[int] = mountain_arr._MountainArray__secret
        try:
            return arr.index(target)
        except:
            return -1
    
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        @cache
        def get(i: int):
            return mountain_arr.get(i)
        
        def find_peak():
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = left + (right - left) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(left, right, is_increasing):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if mid_val < target:
                    if is_increasing:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if is_increasing:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        peak_index = find_peak()
        result = binary_search(0, peak_index, True)
        if result == -1:
            result = binary_search(peak_index + 1, mountain_arr.length() - 1, False)
        return result

# @lc code=end

ma = MountainArray()
solution = Solution()
Input: list[tuple[list[int], int]] = [
    tuple([[1,5,2], 5]),
    tuple([[1,2,3,4,5,3,1], 3]),
]
for array, target in Input:
    print('array:', array, 'target:', target, 'ans:', array.index(target))
    ma._MountainArray__secret = array
    print('Answer:', solution.findInMountainArray(target, ma))
    print('Expected Answer', array.index(target))
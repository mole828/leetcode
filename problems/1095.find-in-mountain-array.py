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

import bisect
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:        
        def get(i: int)->int:return mountain_arr.get(i)
        class MountainList:
            r: bool = False
            def __getitem__(self, i: int)->int:
                return -get(i) if self.r else get(i)
            def __len__(self)->int:
                return mountain_arr.length()
        ml = MountainList()
        def find_peak() -> int:
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = (left + right) // 2
                mid_val = ml[mid]
                if mid_val < ml[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        peak = find_peak()
        index = bisect.bisect_left(ml, target,hi=peak+1)
        if get(index) == target:return index
        ml.r = True
        index = bisect.bisect_left(ml, -target, lo=peak, hi=len(ml)-1)
        return index if get(index) == target else -1
# @lc code=end

ma = MountainArray()
solution = Solution()
Input: list[tuple[list[int], int]] = [
    tuple([[1,5,2], 5]),
    tuple([[1,2,3,4,5,3,1], 3]),
    tuple([[1,5,2], 2]),
    tuple([[1,5,2], 0]),
    tuple([[0,1,2,4,2,1], 3]),
]
for array, target in Input:
    print('array:', array, 'target:', target)
    ma._MountainArray__secret = array
    ans = solution.findInMountainArray(target, ma)
    print('Answer:', ans)
    print('Expected Answer', array.index(target) if target in array else -1)
    print('pass' if (array.index(target) if target in array else -1) == ans else 'error!!!!!!!!')
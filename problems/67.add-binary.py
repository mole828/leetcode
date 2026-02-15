#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def to_bool_arr(s: str) -> list[bool]:
            arr = [c == '1' for c in s]
            arr.reverse()
            return arr
        def arr_to_str(arr: list[bool]) -> str:
            arr.reverse()
            return ''.join('1' if x else '0' for x in arr)
        def arr_add(arr1: list[bool], arr2: list[bool]) -> list[bool]:
            new_arr = []
            carry = False
            for a,b in zip_longest(arr1, arr2, fillvalue=False):
                total = a + b + carry
                new_arr.append(total % 2 == 1)
                carry = total >= 2
            if carry:
                new_arr.append(True)
            return new_arr
        a_arr = to_bool_arr(a)
        b_arr = to_bool_arr(b)
        return arr_to_str(arr_add(a_arr, b_arr))
        
        
# @lc code=end


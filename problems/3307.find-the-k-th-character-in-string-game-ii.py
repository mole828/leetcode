#
# @lc app=leetcode id=3307 lang=python3
#
# [3307] Find the K-th Character in String Game II
#

# @lc code=start
from typing import Callable, List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        arr = [0]
        for operation in operations:
            match operation:
                case 0:
                    arr += arr
                case 1:
                    arr += [v+1 for v in arr]
        return chr(arr[k-1] + 97)
    
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        o0 = lambda x:x
        o1 = lambda x:x+1
        arr: List[Callable[[int], int]] = []
        kk = k
        while len(operations):
            right = 2 ** len(operations)
            left = right // 2
            op = operations.pop()
            print(left, right, op)
            if left < kk <= right:
                kk = kk - left
                print(f"new kk {kk}")
                f = o1 if op else o0
                arr.append(f)
        v = 0
        while arr:
            v = arr.pop()(v)
        return chr(v%26 + 97)
     
# @lc code=end

print(Solution().kthCharacter(5, [0,0,0])) # a
print(Solution().kthCharacter(10, [0,1,0,1])) # b
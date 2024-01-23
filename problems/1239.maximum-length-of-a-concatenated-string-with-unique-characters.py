#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = len(arr)
        @cache
        def setOf(i: int) -> set[str]:
            setOfI = set(arr[i])
            if len(setOfI) == len(arr[i]):
                return setOfI
            return set()
        @cache
        def dp(i: int) -> set[str]:
            if i == length:
                return set()
            iset = setOf(i)
            next = dp(i+1)
            # print(i,iset, next, 1 if not iset&next else 0, iset | next)
            if not iset & next:
                return iset | next
            return iset if len(iset) > len(next) else next
        return len(dp(0))


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = len(arr)
        @cache
        def setOf(i: int) -> set[str]:
            setOfI = set(arr[i])
            if len(setOfI) == len(arr[i]):
                return setOfI
            return set()
        pointer = [0]
        def dp(i: int, has:set[str]):
            # print(i, has)
            if i==length:
                pointer[0] = max(pointer[0], len(has))
                return 
            dp(i+1, has) 
            sumSet = has | setOf(i)
            if len(sumSet) == len(has) + len(setOf(i)):
                dp(i+1, sumSet)
        dp(0, set())
        return pointer[0]
# @lc code=end

print(Solution().maxLength(arr = ["un","iq","ue"]))
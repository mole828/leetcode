#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        has = set()
        for i in range(1,n+1):
            if nums[-i] not in has:
                has.add(nums[-i])
            else:
                break
        print("len(has)", len(has))
        d = n - len(has)
        return d//3 + (1 if d % 3 else 0)
        
# @lc code=end

print(Solution().minimumOperations([4,5,6,4,4]))
print(Solution().minimumOperations([5,7,11,12,12]))
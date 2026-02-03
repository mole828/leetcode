#
# @lc app=leetcode id=3637 lang=python3
#
# [3637] Trionic Array I
#

# @lc code=start
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        i = 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i == 1:
            return False

        i0 = i
        while i < n and nums[i - 1] > nums[i]:
            i += 1
        if i == i0 or i == n: 
            return False

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        return i == n
        
# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.isTrionic([1, 3, 5, 4, 2, 6]))
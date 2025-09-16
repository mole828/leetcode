#
# @lc app=leetcode id=2197 lang=python3
#
# [2197] Replace Non-Coprime Numbers in Array
#

# @lc code=start
from functools import cache
from math import gcd, lcm
from typing import List


class Solution:
    # timeout
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def GCD(a: int, b: int) -> int:
            if b == 0:
                return a
            return GCD(b, a % b)
        def LCM(a: int, b: int) -> int:
            return a * b // GCD(a, b)
        flag = True
        while flag:
            flag = False
            for i in range(len(nums) - 1):
                if GCD(nums[i], nums[i + 1]) > 1:
                    nums[i] = LCM(nums[i], nums[i + 1])
                    nums.pop(i + 1)
                    flag = True
                    break
        return nums
    
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            while st and gcd(x, st[-1]) > 1:
                x = lcm(x, st.pop())
            st.append(x)
        return st
        
# @lc code=end

print(Solution().replaceNonCoprimes([6,4,3,2,7,6,2]))
print(Solution().replaceNonCoprimes([2,2,1,1,3,3,3]))
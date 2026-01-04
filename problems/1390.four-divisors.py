#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_of_divisors(n: int) -> int:
            divisors = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
                if len(divisors) > 4:
                    return 0
            if len(divisors) == 4:
                return sum(divisors)
            return 0

        total_sum = 0
        for num in nums:
            total_sum += sum_of_divisors(num)
        return total_sum
        
# @lc code=end


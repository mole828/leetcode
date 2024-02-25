#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
#

# @lc code=start
from functools import cache
from typing import List

prime_nums = [2]

def primes(_max: int=100000):
    for prime in prime_nums:
        if prime > _max:
            return
        yield prime 
    x = prime_nums[-1] + 1
    while x<=_max:
        for prime in prime_nums:
            if x % prime == 0:
                break 
        else:
            prime_nums.append(x)
            yield x
        x += 1

@cache
def roots(num: int) -> set[int]:
    rs = set()
    for prime in primes(num):
        if num % prime == 0:
            rs.add(prime)
    return rs

# Time Limit Exceeded, 259 / 925 testcases passed
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        length = len(nums)
        sets = [roots(num)for num in nums]
        # print(sets)
        matrix = [[sets[i]&sets[j] for j in range(length)] for i in range(length)]
        # print(matrix)
        @cache
        def connect(i: int, target: int, passed: int = 0) -> bool:
            i_mask = 1<<i 
            if i_mask & passed:
                return False 
            if matrix[i][target]:
                return True 
            for j in range(length):
                if matrix[i][j]:
                    if connect(j,target,passed|i_mask):
                        return True
            return False
        for i in range(length):
            for j in range(i+1, length):
                if not connect(i,j):
                    return False 
        return True
# @lc code=end

print(Solution().canTraverseAllPairs(nums=[2,3,6]))
print(Solution().canTraverseAllPairs(nums=[40,22,15]))
print(Solution().canTraverseAllPairs(nums=[30,50,30,33,30,20,30,30,33]))
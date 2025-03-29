#
# @lc app=leetcode id=2818 lang=python3
# @lcpr version=30204
#
# [2818] Apply Operations to Maximize Score
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List

def solution1():

    primes = [False, False] + [True] * (10 ** 5)
    for i in range(10 ** 5):
        if primes[i]:
            for j in range(i*2, 10 ** 5 + 1, i):
                primes[j] = False
    # print(primes[:100])

    # 分解质数
    def factorize(n: int) -> List[int]:
        factors = []
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                while n % i == 0:
                    factors.append(i)
                    n //= i
        if n > 1:
            factors.append(n)
        return factors

    class Solution:
        def maximumScore(self, nums: List[int], k: int) -> int:

            # 计算每个数的质因数
            factors = [set(factorize(num)) for num in nums]
            # print(factors)
            score_structure = [(len(factors[i]), i, nums[i]) for i in range(len(nums))]
            answer_heap = []
            for left in range(len(nums)):
                for right in range(left, len(nums)):
                    window = score_structure[left:right + 1]
                    max_factors = max(window, key=lambda x: (x[0]))
                    value = max_factors[2] 
                    heapq.heappush(answer_heap, -value)
            # print(answer_heap)
            total = 1
            for i in range(k):
                total *= -heapq.heappop(answer_heap)
                # print(total)
            return total % (10**9 + 7)
    return Solution


def solution2():
    MOD = 10**9 + 7
    MX = 10**5 + 1
    omega = [0] * MX
    for i in range(2, MX):
        if omega[i] == 0:
            for j in range(i, MX, i):
                omega[j] += 1

    class Solution:
        def maximumScore(self, nums: List[int], k: int) -> int:
            n = len(nums)
            left = [-1] * n
            right = [n] * n
            stack = []
            for i,v in enumerate(nums):
                while stack and omega[nums[stack[-1]]] < omega[v]:
                    right[stack.pop()] = i
                if stack: left[i] = stack[-1]
                stack.append(i)
            
            ans = 1
            for i,v,l,r in sorted(zip(range(n), nums, left, right), key=lambda z:-z[1]):
                tot = (i-l)*(r-i)
                if tot >= k:
                    ans = ans * pow(v, k, MOD) % MOD
                    break
                k -= tot
                ans = ans * pow(v, tot, MOD) % MOD
            return ans
    return Solution

Solution = solution2()

# @lc code=end

print(Solution().maximumScore([8, 3, 9, 3, 8], 2))
print(Solution().maximumScore([19, 12, 14, 6, 10, 18], 3))
print(Solution().maximumScore([3289,2832,14858,22011],6))


#
# @lcpr case=start
# [8,3,9,3,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [19,12,14,6,10,18]\n3\n
# @lcpr case=end

#


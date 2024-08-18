#
# @lc app=leetcode id=264 lang=python3
# @lcpr version=
#
# [264] Ugly Number II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache, lru_cache
from heapq import heappop, heappush


# Memory Limit Exceeded, 500/596 cases passed (N/A)
class Solution:
    @cache
    def ugly(num: int) -> bool:
        if num == 1:
            return True
        elif num%2==0:
            return Solution.ugly(num//2)
        elif num%3==0:
            return Solution.ugly(num//3)
        elif num%5==0:
            return Solution.ugly(num//5)
        return False
    def nthUglyNumber(self, n: int) -> int:
        th = 0
        i = 1
        while th < n:
            if Solution.ugly(i):
                th += 1
            i += 1
        return i-1

class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2,3,5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = heappop(uglyHeap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)
        return curr

# @lc code=end

print(Solution().nthUglyNumber(10))

#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


#
# @lc app=leetcode id=3191 lang=python3
#
# [3191] Minimum Operations to Make Binary Array Elements Equal to One I
#

# @lc code=start
import heapq
from math import inf
from typing import List


# Time Limit Exceeded, 20/689 cases passed 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def make_state(nums: List[int]) -> int:
            s = 0
            cur = 1
            for i in range(len(nums)):
                if nums[i] == 1:
                    s |= cur
                cur <<= 1
            return s
        def flip(s: int, begin: int, length: int = 3):
            cur = 1 << begin
            for _ in range(length):
                s ^= cur
                cur <<= 1
            return s
        
        n = len(nums)
        target_state = make_state([1]*n)
        has_meet: set[int] = set()
        heap = [(0, make_state(nums))]
        heapq.heapify(heap)
        while heap:
            deep, this_state = heapq.heappop(heap)
            if this_state in has_meet:
                continue
            has_meet.add(this_state)
            if this_state == target_state:
                return deep
            for i in range(n-2):
                new_state = flip(this_state, i)
                heapq.heappush( heap, (deep+1, new_state,) )
        return -1

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0: 
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans if nums[-2] and nums[-1] else -1

# @lc code=end

print(Solution().minOperations([0,1,1,1,0,0]))
print(Solution().minOperations([0,1,1,1]))
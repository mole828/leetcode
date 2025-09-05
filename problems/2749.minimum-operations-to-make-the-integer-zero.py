#
# @lc app=leetcode id=2749 lang=python3
#
# [2749] Minimum Operations to Make the Integer Zero
#

# @lc code=start
import heapq


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        subs = [2**i+num2 for i in range(61)]
        que = []
        heapq.heapify(que)
        heapq.heappush(que, (abs(num1 - 0), 0, num1))
        has_add = set()
        while que:
            diff, cnt, num = heapq.heappop(que)
            if diff > 2*subs[-1]:
                continue
            if num in has_add:
                continue
            has_add.add(num)
            if num == 0:
                return cnt
            if diff < num:
                return -1
            
            for sub in subs:
                new_num = num - sub
                new_diff = abs(new_num - 0)
                heapq.heappush(que, (new_diff, cnt + 1, new_num))
        return -1
    
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            x = num1 - num2 * k
            if k > x:
                return -1
            if x.bit_count() <= k:
                return k
# @lc code=end

# print(Solution().makeTheIntegerZero(3, -2))
print(Solution().makeTheIntegerZero(5, 7))
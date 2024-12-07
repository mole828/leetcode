#
# @lc app=leetcode id=1760 lang=python3
# @lcpr version=30204
#
# [1760] Minimum Limit of Balls in a Bag
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List

# Wrong Answer
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        final_nums_len = len(nums) + maxOperations
        nums_sum = sum(nums)
        avg = nums_sum // final_nums_len
        nums = [-num for num in nums]
        heapq.heapify(nums)
        last_operations = maxOperations
        while nums and last_operations:
            num = -heapq.heappop(nums)
            last_operations -= 1

            # [431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26]
            # 80
            num -= avg 
            heapq.heappush(nums, -avg)

            # [9] 2
            # half = num // 2 
            # heapq.heappush(nums, -half)
            # num -= half

            heapq.heappush(nums, -num)

        return -heapq.heappop(nums)
        

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(x):
            cnt = 0
            for i in nums:
                cnt += (i-1)//x +1
            return cnt <= (maxOperations+len(nums))
        
        left = 0
        right = max(nums)+1
        while left+1 < right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

# @lc code=end



#
# @lcpr case=start
# [9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,8,2]\n4\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1590 lang=python3
# @lcpr version=
#
# [1590] Make Sum Divisible by P
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums) 
        remainder = total_sum % p 

        if remainder == 0:
            return 0

        def find_smallest_subarray(nums, p, remainder):
            prefix_sum = 0
            min_length = len(nums) 
            prefix_map = {0: -1} 

            for i, num in enumerate(nums):
                prefix_sum += num
                target_remainder = (prefix_sum % p - remainder) % p

                if target_remainder in prefix_map:
                    min_length = min(min_length, i - prefix_map[target_remainder])

                prefix_map[prefix_sum % p] = i

            return min_length

        smallest_subarray_length = find_smallest_subarray(nums, p, remainder)

        return smallest_subarray_length if smallest_subarray_length < len(nums) else -1
        
# @lc code=end



#
# @lcpr case=start
# [3,1,4,2]\n6\n
# @lcpr case=end

# @lcpr case=start
# [6,3,5,2]\n9\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#


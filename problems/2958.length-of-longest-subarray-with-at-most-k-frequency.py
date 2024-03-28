#
# @lc app=leetcode id=2958 lang=python3
# @lcpr version=
#
# [2958] Length of Longest Subarray With at Most K Frequency
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0 
        left, right = 0, 0 
        counter = Counter() 
        length = len(nums)
        while right<length: 
            right_num = nums[right]
            counter[right_num]+=1
            right += 1 
            while counter[right_num]>k:
                # print(counter)
                counter[nums[left]] -= 1
                left += 1 
            # print((left, right))
            max_length = max(max_length, right - left)
        return max_length
# @lc code=end

print(Solution().maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
print(Solution().maxSubarrayLength([2,11], 1))

#
# @lcpr case=start
# [1,2,3,1,2,3,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5,5,5,5]\n4\n
# @lcpr case=end

#


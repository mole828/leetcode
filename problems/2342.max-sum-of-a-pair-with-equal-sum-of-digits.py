#
# @lc app=leetcode id=2342 lang=python3
# @lcpr version=30204
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count_of_digits = defaultdict(list)
        for num in nums:
            count_of_digits[sum(map(int, str(num)))].append(num)
        max_sum = -1
        for k, v in count_of_digits.items():
            if len(v) > 1:
                max_sum = max(max_sum, sum(sorted(v)[-2:]))
        return max_sum
        
# @lc code=end



#
# @lcpr case=start
# [18,43,36,13,7]\n
# @lcpr case=end

# @lcpr case=start
# [10,12,19,14]\n
# @lcpr case=end

#


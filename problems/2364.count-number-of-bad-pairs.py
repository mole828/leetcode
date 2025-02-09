#
# @lc app=leetcode id=2364 lang=python3
# @lcpr version=30204
#
# [2364] Count Number of Bad Pairs
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


# Time Limit Exceeded
# 51/65 cases passed (N/A)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if j - i != b - a:
                    bad_pairs += 1
        return bad_pairs


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        sub_count = Counter()
        for i,v in enumerate(nums):
            sub = v - i
            bad_pairs += i - sub_count[sub]
            sub_count[sub] += 1
        return bad_pairs


# @lc code=end

print(Solution().countBadPairs([4,1,3,3]))

#
# @lcpr case=start
# [4,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#


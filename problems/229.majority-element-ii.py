#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        base = len(nums)/3
        return [key for key in count.keys() if count[key]>base]
            
# @lc code=end
print(Solution().majorityElement([1,3]))


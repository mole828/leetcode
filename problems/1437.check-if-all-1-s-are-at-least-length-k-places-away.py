#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one_index - 1 < k:
                    return False
                last_one_index = i
        return True
        
# @lc code=end


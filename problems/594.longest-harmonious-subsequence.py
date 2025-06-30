#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for num in counter:
            if num + 1 in counter:
                ans = max(ans, counter[num] + counter[num + 1])
        return ans

        
# @lc code=end


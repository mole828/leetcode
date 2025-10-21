#
# @lc app=leetcode id=3346 lang=python3
#
# [3346] Maximum Frequency of an Element After Performing Operations I
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1

        ans = sum_d = 0
        for x, d in sorted(diff.items()):
            sum_d += d
            ans = max(ans, min(sum_d, cnt[x] + numOperations))
        return ans
        
# @lc code=end

print(Solution().maxFrequency([1,4,5], 1, 2))
print(Solution().maxFrequency([88, 53], 27, 2))
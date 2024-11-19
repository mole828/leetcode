#
# @lc app=leetcode id=2461 lang=python3
# @lcpr version=
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = Counter()
        ws = 0
        max_sum = 0

        for i in range(n):
            mp[nums[i]] += 1
            ws += nums[i]

            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum

        
# @lc code=end



#
# @lcpr case=start
# [1,5,4,2,9,9,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4]\n3\n
# @lcpr case=end

#


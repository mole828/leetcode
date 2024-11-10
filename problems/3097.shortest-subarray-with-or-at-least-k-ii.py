#
# @lc app=leetcode id=3097 lang=python3
# @lcpr version=30204
#
# [3097] Shortest Subarray With OR at Least K II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        l = v = 0
        c = [0] * 30

        def add(num):
            for i in range(30):
                c[i] += num >> i & 1

        def reduce(v, num):
            for i in range(30):
                c[i] -= num >> i & 1
                if (v >> i & 1) > c[i]:
                    v ^= 1 << i
            return v

        ans = math.inf
        for i, num in enumerate(nums):
            v |= num
            add(num)
            while v >= k:
                ans = min(ans, i - l + 1)
                v = reduce(v, nums[l])
                l += 1
        return ans if ans < math.inf else -1
        
# @lc code=end

print(Solution().minimumSubarrayLength([1, 2, 32, 21], 55))

#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,8]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#


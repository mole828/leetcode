#
# @lc app=leetcode id=3578 lang=python3
# @lcpr version=30204
#
# [3578] Count Partitions With Max-Min Difference at Most K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def dfs(i: int) -> int:
            # print("call", i)
            if i == n:
                return 1
            this_min = nums[i]
            this_max = nums[i]
            ans = 0
            for j in range(i, n):
                # this_min = min(this_min, nums[j])
                # this_max = max(this_max, nums[j])
                this_min = this_min if nums[j] >= this_min else nums[j]
                this_max = this_max if nums[j] <= this_max else nums[j]
                # print(i,j, this_min, this_max)
                if this_max - this_min <= k:
                    ans += dfs(j+1)
            return ans % MOD
        return dfs(0) % MOD


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()
        
        dp[0] = 1
        prefix[0] = 1
        
        j = 0
        for i in range(n):
            cnt.add(nums[i])
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        
        return dp[n]

# @lc code=end

print(Solution().countPartitions([9,4,1,3,7], 4))  # Expected output: 6

#
# @lcpr case=start
# [9,4,1,3,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,3,4]\n0\n
# @lcpr case=end

#


#
# @lc app=leetcode id=2597 lang=python3
# @lcpr version=
#
# [2597] The Number of Beautiful Subsets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = []
        def dfs(i: int, s: set[int]):
            if i == len(nums):
                if s:
                    result.append(s)
                return
            v = nums[i]
            dfs(i+1, s)
            if (v-k) not in s and (v+k) not in s:
                dfs(i+1, s|{v})
        dfs(0, set())
        return len(result)
# @lc code=end

print(Solution().beautifulSubsets([2,4,6], 2))

#
# @lcpr case=start
# [2,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#


#
# @lc app=leetcode id=2099 lang=python3
# @lcpr version=30204
#
# [2099] Find Subsequence of Length K With the Largest Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = sorted(zip(nums, range(n)), key=lambda x: x[0], reverse=True)
        arr = arr[:k]
        arr.sort(key=lambda x: x[1])
        return [x[0] for x in arr]
        
# @lc code=end



#
# @lcpr case=start
# [2,1,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,3,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,4,3,3]\n2\n
# @lcpr case=end

#


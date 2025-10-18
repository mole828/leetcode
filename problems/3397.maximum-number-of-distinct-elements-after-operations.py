#
# @lc app=leetcode id=3397 lang=python3
# @lcpr version=30204
#
# [3397] Maximum Number of Distinct Elements After Operations
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        # num_set = set()
        ans = 0
        pre = float('-inf')
        for num in nums:
            new_num = min(max(num-k, pre+1), num+k)
            if new_num > pre:
                # num_set.add(new_num)
                ans += 1
                pre = new_num
        # return len(num_set)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,3,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4,4]\n1\n
# @lcpr case=end

#


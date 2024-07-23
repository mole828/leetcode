#
# @lc app=leetcode id=1636 lang=python3
# @lcpr version=
#
# [1636] Sort Array by Increasing Frequency
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for k,v in sorted(count.items(), key=lambda t:(t[1],-t[0])):
            ans += [k]*v
        return ans
# @lc code=end

print(Solution().frequencySort([1,1,2,2,2,3]))

#
# @lcpr case=start
# [1,1,2,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,-6,4,5,-6,1,4,1]\n
# @lcpr case=end

#


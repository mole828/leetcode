#
# @lc app=leetcode id=786 lang=python3
# @lcpr version=
#
# [786] K-th Smallest Prime Fraction
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        value_tuple = [(arr[i]/arr[j], [arr[i],arr[j]]) for i in range(len(arr)) for j in range(i+1, len(arr))]
        value_tuple.sort()
        return value_tuple[k-1][1]
# @lc code=end

print(Solution().kthSmallestPrimeFraction([1,2,3,5],3))

#
# @lcpr case=start
# [1,2,3,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,7]\n1\n
# @lcpr case=end

#


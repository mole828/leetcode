#
# @lc app=leetcode id=3068 lang=python3
# @lcpr version=
#
# [3068] Find the Maximum Sum of Node Values
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 353/717 cases passed (N/A)
    def _maximumValueSum(self, nums: List[int], k: int, edges: List[tuple[int,int]]) -> int:
        def mask2nums(mask: int) -> list[int]:
            i = 0
            new_nums = nums.copy()
            while mask:
                if mask & 1:
                    a,b = edges[i]
                    new_nums[a] ^= k
                    new_nums[b] ^= k
                mask >>= 1
                i += 1
            return new_nums
        def dp(i: int, mask: int) -> int:
            if i == len(edges):
                sum_of_mask = sum(mask2nums(mask))
                return sum_of_mask
            return max(dp(i+1, mask), dp(i+1, mask|(1<<i)))
        return dp(0,0)
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalSum = 0
        count = 0
        positiveMin = float("inf")
        negativeMax = float("-inf")

        for nodeValue in nums:
            nodeValAfterOperation = nodeValue ^ k

            totalSum += nodeValue
            netChange = nodeValAfterOperation - nodeValue

            if netChange > 0:
                positiveMin = min(positiveMin, netChange)
                totalSum += netChange
                count += 1
            else:
                negativeMax = max(negativeMax, netChange)

        if count % 2 == 0:
            return totalSum
        return int(max(totalSum - positiveMin, totalSum + negativeMax))


# @lc code=end

print(Solution().maximumValueSum([1,2,1], 3, [[0,1],[0,2]]))

#
# @lcpr case=start
# [1,2,1]\n3\n[[0,1],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [2,3]\n7\n[[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7]\n3\n[[0,1],[0,2],[0,3],[0,4],[0,5]]\n
# @lcpr case=end

#


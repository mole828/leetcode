#
# @lc app=leetcode id=1829 lang=python3
# @lcpr version=
#
# [1829] Maximum XOR for Each Query
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = 2 ** maximumBit - 1
        xor = reduce(lambda x, y: x ^ y, nums)
        ans = []
        for x in reversed(nums):
            y = xor ^ m
            ans.append(y)
            xor ^= x
        return ans
        
# @lc code=end

print( 0^1^1^3^0 )
print(Solution().getMaximumXor([0,1,1,3], 2))

#
# @lcpr case=start
# [0,1,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,5,7]\n3\n
# @lcpr case=end

#


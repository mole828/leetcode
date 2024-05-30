#
# @lc app=leetcode id=1442 lang=python3
# @lcpr version=
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from typing import List


class Solution:
    # Time Limit Exceeded, 41/47 cases passed (N/A)
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a = reduce(lambda x,y:x^y, arr[i:j])
                for k in range(j, len(arr)):
                    b = reduce(lambda x,y:x^y, arr[j:k+1])
                    if a == b:
                        print((i,j,k))
                        count += 1
        return count
        
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            a = arr[i]
            for j in range(i+1, len(arr)):
                b = 0
                for k in range(j, len(arr)):
                    b ^= arr[k]
                    if a == b:
                        # print((i,j,k))
                        count += 1
                a ^= arr[j]
            a ^= arr[i]
        
        return count
# @lc code=end

print(Solution().countTriplets([2,3,1,6,7]))

#
# @lcpr case=start
# [2,3,1,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

#


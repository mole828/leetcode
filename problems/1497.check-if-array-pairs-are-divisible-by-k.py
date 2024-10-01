#
# @lc app=leetcode id=1497 lang=python3
# @lcpr version=
#
# [1497] Check If Array Pairs Are Divisible by k
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        for a in arr:
            count[a % k] += 1

        for i in range(1, k):
            if count[i]!= count[k - i]:
                return False

        return count[0] % 2 == 0
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,10,6,7,8,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n10\n
# @lcpr case=end

#


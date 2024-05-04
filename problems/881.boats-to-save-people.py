#
# @lc app=leetcode id=881 lang=python3
# @lcpr version=
#
# [881] Boats to Save People
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        while people:
            a = people.pop(0)
            ib = bisect.bisect_right(people, limit-a)
            if ib:
                people.pop(ib-1)
            boats += 1
        return boats
                
# @lc code=end

print(Solution().numRescueBoats([3,5,3,4], 5))
print(Solution().numRescueBoats([5,1,4,2], 6))

#
# @lcpr case=start
# [1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,5,3,4]\n5\n
# @lcpr case=end

#


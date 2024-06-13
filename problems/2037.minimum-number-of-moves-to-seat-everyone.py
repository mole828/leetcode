#
# @lc app=leetcode id=2037 lang=python3
# @lcpr version=
#
# [2037] Minimum Number of Moves to Seat Everyone
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(a-b) for a,b in zip(sorted(seats), sorted(students)))
# @lc code=end



#
# @lcpr case=start
# [3,1,5]\n[2,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,5,9]\n[1,3,2,6]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,6,6]\n[1,3,2,6]\n
# @lcpr case=end

#


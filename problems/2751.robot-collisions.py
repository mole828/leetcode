#
# @lc app=leetcode id=2751 lang=python3
# @lcpr version=
#
# [2751] Robot Collisions
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[stack[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[stack.pop()] = 0
                if stack:
                    if healths[stack[-1]] == healths[i]:
                        healths[stack.pop()] = 0
                    else:
                        healths[stack[-1]] -= 1
                    healths[i] = 0
        return [h for h in healths if h]
 
# @lc code=end



#
# @lcpr case=start
# [5,4,3,2,1]\n[2,17,9,15,10]\n"RRRRR"\n
# @lcpr case=end

# @lcpr case=start
# [3,5,2,6]\n[10,10,15,12]\n"RLRL"\n
# @lcpr case=end

# @lcpr case=start
# [1,2,5,6]\n[10,10,11,11]\n"RLRL"\n
# @lcpr case=end

#


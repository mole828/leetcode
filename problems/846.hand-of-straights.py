#
# @lc app=leetcode id=846 lang=python3
# @lcpr version=
#
# [846] Hand of Straights
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand = sorted(hand)
        while hand:
            group = [hand.pop(0)]
            while len(group) < groupSize:
                target = group[-1] + 1
                try:
                    hand.remove(target)
                except:
                    return False
                group.append(target)
        return True
# @lc code=end



#
# @lcpr case=start
# [1,2,3,6,2,3,4,7,8]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n4\n
# @lcpr case=end

#


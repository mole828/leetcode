#
# @lc app=leetcode id=2410 lang=python3
# @lcpr version=30204
#
# [2410] Maximum Matching of Players With Trainers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
            j += 1
        return i
        
# @lc code=end



#
# @lcpr case=start
# [4,7,9]\n[8,2,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n[10]\n
# @lcpr case=end

#


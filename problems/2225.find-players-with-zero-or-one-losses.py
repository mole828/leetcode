#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        winCount = defaultdict(int)
        lossCount = defaultdict(int)
        for win,loss in matches:
            players.add(win)
            players.add(loss)
            winCount[win] += 1
            lossCount[loss] += 1
        loss1 = set()
        hasLoss = set()
        for key in lossCount:
            hasLoss.add(key)
            lossTime = lossCount[key]
            if lossTime == 1:
                loss1.add(key)
        loss0 = players - hasLoss
        return [
            sorted(list(loss0)),
            sorted(list(loss1))
        ]
# @lc code=end


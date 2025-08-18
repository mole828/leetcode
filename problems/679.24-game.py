#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from itertools import permutations, product
from typing import List, Union

EPS = 1e-9
class Solution:
    def judgePoint24(self, cards: List[Union[int, float]]) -> bool:
        n = len(cards)
        if n == 1:
            return abs(cards[0] - 24) < EPS
        for i, x in enumerate(cards):
            for j in range(i+1, n):
                y = cards[j]
                candidates = [x+y, x-y, y-x, x*y]
                if abs(y) > EPS:
                    candidates.append(x/y)
                if abs(x) > EPS:
                    candidates.append(y/x)
                
                new_cards = cards.copy()
                new_cards.remove(x)
                new_cards.remove(y)
                for candidate in candidates:
                    new_cards.append(candidate)
                    if self.judgePoint24(new_cards):
                        return True
                    new_cards.remove(candidate)
        return False


# link https://leetcode.cn/problems/24-game/solutions/3756006/mei-ci-he-bing-liang-zhang-pai-di-gui-xi-0sdu/
        
# @lc code=end

print(Solution().judgePoint24([4, 1, 8, 7]))

# @lc app=leetcode id=950 lang=python3
# @lcpr version=
#
# [950] Reveal Cards In Increasing Order
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() 
        result = [deck.pop()] 
        while deck:
            result.insert(0, result.pop()) 
            result.insert(0, deck.pop()) 
        return result
# @lc code=end

def check(deck: List[int]):
    while deck:
        print(deck.pop(0))
        if deck:
            deck.append(deck.pop(0))
check([2,13,3,11,5,17,7])

#
# @lcpr case=start
# [17,13,11,2,3,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1000]\n
# @lcpr case=end

#


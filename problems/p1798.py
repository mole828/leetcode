from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        sum = 0
        for c in coins:
            if c - sum > 1:
                break
            else:
                sum += c
        return sum + 1
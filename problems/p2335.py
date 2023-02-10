from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a = max(amount)
        b = sum(amount)
        c = sum(amount) - a 
        return a if a > c else b//2+b%2
            
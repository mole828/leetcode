from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans, last = 0, 0
        for (x,rate) in brackets:
            if income <= last:break
            ans += (min(income,x)-last)*rate/100.0
            last = x
        return ans

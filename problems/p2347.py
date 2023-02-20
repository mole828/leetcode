from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        countColor = Counter(suits)
        if any(countColor[color]==5 for color in countColor):return "Flush"
        countNum = Counter(ranks)
        if any(countNum[num]>=3 for num in countNum):return "Three of a Kind"
        if any(countNum[num]>=2 for num in countNum):return "Pair"
        return "High Card"
        
        
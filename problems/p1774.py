from typing import List


class Solution:
    def get_n_nary(self, num:int, n:int, least_length:int):
        results = []
        while num:
            results.append(num % n)
            num //= n
        while len(results) < least_length:
            results.append(0)
        return results[::-1]

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(toppingCosts)
        results = []
        threes = [self.get_n_nary(num, 3, n) for num in range(3 ** n)]
        for baseCost in baseCosts:
            for three in threes:
                toppingCost = sum([toppingCosts[index] * count for index, count in enumerate(three)])
                results.append(toppingCost + baseCost)
        return min(results, key=lambda x: (abs(target - x), x))
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        maxE = sum(energy)
        res = 0
        if maxE>=initialEnergy:
            res+=(maxE-initialEnergy+1)
        for i in experience:
            if initialExperience>i:
                initialExperience+=i
            else:
                res+=(i+1-initialExperience)
                initialExperience = i+i+1
        return res
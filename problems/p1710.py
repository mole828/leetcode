from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        ans = 0
        for box in boxTypes:
            size = min(box[0], truckSize)
            truckSize -= size
            ans += size * box[1]
            if truckSize==0:break
        return ans
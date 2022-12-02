from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(x) for x in boxes]
        ans = [sum(boxes[j]*abs(i-j) for j in range(len(boxes)) if i!=j) for i in range(len(boxes))]
        return ans
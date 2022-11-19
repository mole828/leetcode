from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        h = 0
        for dh in gain:
            h += dh
            ans = max(ans, h)
        return ans
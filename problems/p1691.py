from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n=len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(reverse=True)
        h=[0]*n
        for i in range(n):
            for j in range(i):
                if cuboids[j][1]>=cuboids[i][1] and cuboids[j][2]>=cuboids[i][2]:
                    h[i]=max(h[i],h[j])
            h[i]+=cuboids[i][2]
        return max(h)
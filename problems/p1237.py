
from typing import List


class CustomFunction:
    def f(self, x, y)->int:pass

class Solution:
    def findSolution(self, customfunction: CustomFunction, z: int) -> List[List[int]]:
        y, g = z, customfunction.f
        for x in range(1, z + 1):
            while y:
                d = g(x, y) - z
                if d <= 0:
                    if not d:
                        yield [x, y]
                    break
                y -= 1
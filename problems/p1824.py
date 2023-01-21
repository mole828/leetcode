from typing import List
from numpy import Inf

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        ans = [1,0,1]
        for ob in obstacles:
            ob = ob-1
            last = ans
            stage = [min(
                max(Inf if j==ob else 0 , last[j]) + (1 if i!=j else 0) for j in range(3)
            ) if i!=ob else Inf for i in range(3)]
            ans = stage
        return min(ans)

    
if __name__ == '__main__':
    Solution().minSideJumps(obstacles = [0,1,2,3,0])



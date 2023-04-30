from functools import cache
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def dfs(x: int) -> int:
            if manager[x] < 0:
                return informTime[x]
            return dfs(manager[x]) + informTime[x]
        return max(dfs(i) for i in range(n))



if __name__ == '__main__':
    assert Solution().numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]) == 0
    assert Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]) == 1
    assert Solution().numOfMinutes(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1]) == 21

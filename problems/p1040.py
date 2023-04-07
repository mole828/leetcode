from functools import cache
from typing import List


class Solution0:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        ans = []
        stones.sort()
        @cache
        def dfs(stones:List[int], times:int=0)->int:
            ans = []
            without_left = stones[1:]
            for i in range(without_left[0],without_left[-1]):
                if i not in without_left:
                    ans.append(dfs(sorted(without_left + [i]), times+1))
            without_right = stones[:-1]
            for i in range(without_right[0],without_right[-1]):
                if i not in without_right:
                    ans.append(dfs(sorted(without_right + [i]), times+1))
            return min(ans) if ans else times
        ans.append(dfs(stones))
        @cache
        def dfs(stones:List[int], times:int=0)->int:
            ans = []
            without_left = stones[1:]
            print(f"without_left: {without_left}")
            for i in range(without_left[0],without_left[-1]):
                if i not in without_left:
                    ans.append(dfs(sorted(without_left + [i]), times+1))
            without_right = stones[:-1]
            for i in range(without_right[0],without_right[-1]):
                if i not in without_right:
                    ans.append(dfs(sorted(without_right + [i]), times+1))
            return max(ans) if ans else times
        ans.append(dfs(stones))
        return ans

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        mi = n = len(stones)
        mx = max(stones[-1] - stones[1] + 1, stones[-2] - stones[0] + 1) - (n - 1)
        i = 0
        for j, x in enumerate(stones):
            while x - stones[i] + 1 > n:
                i += 1
            if j - i + 1 == n - 1 and x - stones[i] == n - 2:
                mi = min(mi, 2)
            else:
                mi = min(mi, n - (j - i + 1))
        return [mi, mx]

if __name__ == '__main__':
    print(Solution().numMovesStonesII([7,4,9]))
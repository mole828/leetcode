from collections import defaultdict
import pprint
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        m = defaultdict(list[int])
        for u, v in paths:
            m[u].append(v)
            m[v].append(u)
        ans = [0]*n
        pprint.pprint(m)
        for u in range(1, n + 1):
            colors = set(range(1, 5)) - set(ans[v - 1] for v in m[u])
            ans[u - 1] = colors.pop()
            # pprint.pprint(ans)
        return ans

if __name__ == '__main__':
    print(Solution().gardenNoAdj(n = 3, paths = [[1,2],[2,3],[3,1]]))
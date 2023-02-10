from functools import lru_cache
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        mod = 10 ** 9 + 7


        @lru_cache(None)
        def dfs(k, a1,a2,a3,a4,a5,a6,pre):
            if k == n:
                return 1
            
            ret = 0
            
            for i in range(1, 7):
                if i == pre:
                    if i == 1 and a1+1<=rollMax[0]:
                        ret+=dfs(k+1,a1+1,0,0,0,0,0,i)
                    elif i == 2 and a2+1<=rollMax[1] :
                        ret+=dfs(k+1,0,a2+1,0,0,0,0,i)
                    elif i == 3 and a3+1<=rollMax[2]:
                        ret+=dfs(k+1,0,0,a3+1,0,0,0,i)
                    elif i == 4 and a4+1<=rollMax[3]:
                        ret+=dfs(k+1,0,0,0,a4+1,0,0,i)
                    elif i == 5 and a5+1<=rollMax[4]:
                        ret+=dfs(k+1,0,0,0,0,a5+1,0,i)
                    elif i == 6 and a6+1<=rollMax[5]:
                        ret+=dfs(k+1,0,0,0,0,0,a6+1,i)
                    else:
                        continue
                else:
                    if i == 1:
                        ret += dfs(k+1,1,0,0,0,0,0,i)
                    elif i == 2:
                        ret += dfs(k+1,0,1,0,0,0,0,i)
                    elif i == 3:
                        ret += dfs(k+1,0,0,1,0,0,0,i)
                    elif i == 4:
                        ret += dfs(k+1,0,0,0,1,0,0,i)
                    elif i == 5:
                        ret += dfs(k+1,0,0,0,0,1,0,i)
                    elif i == 6:
                        ret += dfs(k+1,0,0,0,0,0,1,i)
                ret %= mod
            return ret

        return dfs(0,0,0,0,0,0,0,-1)
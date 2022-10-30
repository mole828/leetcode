from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def dfs (temp:str= '', start:int= 0):
            if len(temp) == len(s):
                ans.append(temp)
                return
            c = s[start]
            if c.isdigit():
                dfs(temp+c, start+1)
            else:
                dfs(temp+c, start+1)
                dfs(temp+(c.upper() if c.islower() else c.lower()), start+1)
        dfs()
        return ans
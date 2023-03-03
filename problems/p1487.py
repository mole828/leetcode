from collections import defaultdict
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        namemap = {}
        for name in names:
            s = name
            while s in namemap:
                s = f"{name}({namemap[name]})"
                namemap[name]+=1
            namemap[s]=1
            ans.append(s)
        return ans
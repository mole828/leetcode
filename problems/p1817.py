from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], lenOfAns: int) -> List[int]:
        m = defaultdict(list)
        for k,v in logs:
            if v not in m[k]:
                m[k].append(v)
        print(m)
        ans = [0 for _ in range(lenOfAns)]
        print(ans)
        for k in m:
            print(k,m[k],len(m[k]))    
            ans[len(m[k])-1] += 1
        return ans

if __name__ == '__main__':
    Solution().findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], lenOfAns = 5)
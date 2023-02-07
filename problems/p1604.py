from collections import defaultdict
from typing import List
from sortedcontainers import SortedList

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timesMap = defaultdict(SortedList)
        for (name,time) in zip(keyName, keyTime):
            h,m = [int(s) for s in time.split(':')]
            timesMap[name].add(h*60+m)
        print(timesMap)
        ans = []
        for name in timesMap.keys():
            if len(timesMap[name])>=3:
                all = timesMap[name]
                for i in range(len(all)-2):
                    a,b = all[i],all[i+2]
                    print(a,b)
                    if b-a<=60:
                        ans.append(name)
                        break
        return sorted(ans)

if __name__ == '__main__':
    Solution().alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic,count,start,end={0:0},0,0,0
        for i in range(len(array)):
            count+=1 if array[i].isdigit() else -1
            if count in dic:
                a=dic[count]
                if i+1-a>end-start:
                    start,end=a,i+1
            else:
                dic[count]=i+1
        return array[start:end]
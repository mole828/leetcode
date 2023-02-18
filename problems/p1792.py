from typing import List
from sortedcontainers import SortedList
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def dr(nPass,nSum):
            return (nPass+1)/(nSum+1) - nPass/nSum
        classes = SortedList([[nPass, nSum, dr(nPass,nSum)] for (nPass, nSum) in classes], key=lambda i:i[2])
        for _ in range(extraStudents):
            [nPass, nSum, _] = classes.pop()
            nPass += 1
            nSum += 1 
            classes.add([nPass,nSum,dr(nPass,nSum)])
        
        return sum( nPass/nSum for [nPass,nSum,_] in classes ) / len(classes)

if __name__ == '__main__':
    Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
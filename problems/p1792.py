from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def dr(nPass,nSum):
            return (nPass+1)/(nSum+1) - nPass/nSum
        classes = [(-dr(nPass,nSum), nPass, nSum, ) for (nPass, nSum) in classes]
        heapq.heapify(classes)
        for _ in range(extraStudents):
            print(classes)
            [_, nPass, nSum, ] = heapq.heappop(classes)
            nPass += 1
            nSum += 1 
            heapq.heappush(classes, (-dr(nPass,nSum),nPass,nSum,) )
        return sum( nPass/nSum for [_,nPass,nSum,] in classes ) / len(classes)

if __name__ == '__main__':
    Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
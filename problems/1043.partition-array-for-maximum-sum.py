#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
from typing import List

# Wrong Answer
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        length = len(arr)
        newarr = [0]*length
        for i,v in enumerate(arr):
            left, right = max(0,i-k+1), min(length, i+k-1)
            for j in range(left, right):
                newarr[j] = max(newarr[j],arr[i])
        print(newarr)
        return sum(newarr)
    
class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        N = len(arr)
        K = k + 1

        dp = [0] * K

        for start in range(N - 1, -1, -1):
            curr_max = 0
            end = min(N, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + curr_max * (i - start + 1))
                print(dp)
        print(dp)
        return dp[0]

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        length = len(arr)
        dp = [0]*(length+1)
        for i in range(1, len(dp)):
            curmaxi, best = 0, 0
            for j in range(1,k+1):
                if j<=i:
                    curmaxi = max(curmaxi, arr[i-j])
                    best = max(best, dp[i-j]+curmaxi*j)
            dp[i] = best 
        return dp[length]
# @lc code=end

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10],3))
# print(Solution().maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))

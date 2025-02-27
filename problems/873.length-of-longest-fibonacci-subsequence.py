#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        after = set(arr)
        n = len(arr)
        ans = 0
        for i in range(n):
            iv = arr[i]
            for j in range(i+1, n):
                jv = arr[j]
                count = 2
                while iv + jv in after:
                    iv, jv = jv, iv + jv
                    count += 1
                    # print(iv, jv, count)
                ans = max(ans, count)
                iv = arr[i]
        return ans if ans > 2 else 0
        
        
# @lc code=end

print(Solution().lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
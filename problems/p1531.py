from collections import Counter
from functools import cache
from math import log10
from sortedcontainers import SortedList
class Solution:
    @cache
    def __compress(s: str) -> str:
        left = 0
        right = 0
        output = ''
        while right < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            sub = s[left:right]
            if len(sub) > 1:
                sub = sub[0] + str(len(sub))
            left = right
            output += sub 
        return output
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        print(dp)
        return dp[n][k]
    
if __name__ == '__main__':
    print(Solution().getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
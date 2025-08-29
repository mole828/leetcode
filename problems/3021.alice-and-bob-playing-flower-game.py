#
# @lc app=leetcode id=3021 lang=python3
#
# [3021] Alice and Bob Playing Flower Game
#

# @lc code=start
class Solution:
    # Time Limit Exceeded
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if (i + j) % 2 == 1:
                    ans += 1
        return ans 
    
    def flowerGame(self, n: int, m: int) -> int:
        return (n * m) // 2
# @lc code=end


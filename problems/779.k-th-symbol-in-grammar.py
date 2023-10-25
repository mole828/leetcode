#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start

ref = {
    '0': '01',
    '1': '10',
}

def gra(n: int) -> str:
    return '0' if n == 0 else ref[gra(n//2)][n%2]

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return int(gra(k-1))
        
# @lc code=end

#
# @lc app=leetcode id=2048 lang=python3
#
# [2048] Next Greater Numerically Balanced Number
#

# @lc code=start
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num: int) -> bool:
            count = [0]*10
            for c in str(num):
                count[int(c)] += 1
            if count[0]:
                return False
            for i in range(1, 10):
                if count[i] and count[i] != i:
                    return False
            return True
        candidate = n + 1
        while True:
            if is_balanced(candidate):
                return candidate
            candidate += 1
        
# @lc code=end


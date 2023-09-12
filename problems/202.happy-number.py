#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        path = []
        while n not in path:
            path.append(n)
            n = sum([int(c)**2 for c in str(n)])
            # print(path)
        return 1 in path 
        
# @lc code=end


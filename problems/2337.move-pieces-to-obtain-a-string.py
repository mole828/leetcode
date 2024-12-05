#
# @lc app=leetcode id=2337 lang=python3
# @lcpr version=
#
# [2337] Move Pieces to Obtain a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        i = j = 0
        n = len(start)
        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i < n and j < n and (start[i] == 'L' and i < j or start[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
        return True
# @lc code=end



#
# @lcpr case=start
# "_L__R__R_"\n"L______RR"\n
# @lcpr case=end

# @lcpr case=start
# "R_L_"\n"__LR"\n
# @lcpr case=end

# @lcpr case=start
# "_R"\n"R_"\n
# @lcpr case=end

#


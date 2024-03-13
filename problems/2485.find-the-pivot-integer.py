#
# @lc app=leetcode id=2485 lang=python3
# @lcpr version=
#
# [2485] Find the Pivot Integer
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        a = 1
        x = n  
        b = n 
        ax = sum(range(a,x+1))
        xb = sum(range(x,b+1))
        while ax>xb:
            ax -= x 
            x -= 1 
            xb += x 
            print(ax,xb)
        if ax==xb:
            return x 
        return -1

        
# @lc code=end



#
# @lcpr case=start
# 8\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#


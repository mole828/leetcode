#
# @lc app=leetcode id=1137 lang=python3
# @lcpr version=
#
# [1137] N-th Tribonacci Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    m = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
    }
    def tribonacci(self, n: int) -> int:
        if n not in self.m:
            self.m[n] = sum([
                self.tribonacci(n-1),
                self.tribonacci(n-2),
                self.tribonacci(n-3),
            ])
        return self.m[n]
        
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 25\n
# @lcpr case=end

#


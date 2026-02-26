#
# @lc app=leetcode id=1404 lang=python3
# @lcpr version=
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, base=2)
        step = 0
        while n != 1:
            step += 1
            if n & 1:
                n += 1
            else:
                n >>= 1
        return step
            
# @lc code=end
if __name__ == "__main__":
    pass


#
# @lcpr case=start
# "1101"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

# @lcpr case=start
# "1"\n
# @lcpr case=end

#


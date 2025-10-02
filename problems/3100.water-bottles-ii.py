#
# @lc app=leetcode id=3100 lang=python3
# @lcpr version=30204
#
# [3100] Water Bottles II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        bottles_drank = 0
        while full_bottles or empty_bottles >= numExchange:
            if full_bottles:
                bottles_drank += full_bottles
                empty_bottles += full_bottles
                full_bottles = 0
            elif empty_bottles >= numExchange:
                empty_bottles -= numExchange
                full_bottles += 1
                numExchange += 1
        return bottles_drank
        
# @lc code=end



#
# @lcpr case=start
# 13\n6\n
# @lcpr case=end

# @lcpr case=start
# 10\n3\n
# @lcpr case=end

#


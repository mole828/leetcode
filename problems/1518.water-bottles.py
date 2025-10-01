#
# @lc app=leetcode id=1518 lang=python3
# @lcpr version=
#
# [1518] Water Bottles
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 2025-10-01 day2
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        full_bottles = numBottles
        empty_bottles = 0
        while full_bottles:
            drink += full_bottles
            empty_bottles += full_bottles
            full_bottles = 0

            full_bottles += empty_bottles // numExchange
            empty_bottles %= numExchange

        return drink
# @lc code=end



#
# @lcpr case=start
# 9\n3\n
# @lcpr case=end

# @lcpr case=start
# 15\n4\n
# @lcpr case=end

#


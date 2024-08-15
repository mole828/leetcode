#
# @lc app=leetcode id=860 lang=python3
# @lcpr version=
#
# [860] Lemonade Change
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else: # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
# @lc code=end



#
# @lcpr case=start
# [5,5,5,10,20]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,10,10,20]\n
# @lcpr case=end

#


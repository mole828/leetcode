#
# @lc app=leetcode id=2683 lang=python3
# @lcpr version=
#
# [2683] Neighboring Bitwise XOR
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/neighboring-bitwise-xor/solutions/2269241/tui-gong-shi-by-endlesscheng-90t5/
        
# @lc code=end



#
# @lcpr case=start
# [1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0]\n
# @lcpr case=end

#


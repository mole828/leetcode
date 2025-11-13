#
# @lc app=leetcode id=3228 lang=python3
# @lcpr version=30204
#
# [3228] Maximum Number of Operations to Move Ones to the End
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import re


class Solution:
    def maxOperations(self, s: str) -> int:    
        s = re.sub(r'0+', '0', s)
        one_count = 0
        res = 0
        for v in s: 
            match v:
                case '0':
                    res += one_count
                case '1':
                    one_count += 1
        return res

# @lc code=end



#
# @lcpr case=start
# "1001101"\n
# @lcpr case=end

# @lcpr case=start
# "00111"\n
# @lcpr case=end

#


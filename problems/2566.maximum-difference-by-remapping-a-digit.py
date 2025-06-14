#
# @lc app=leetcode id=2566 lang=python3
# @lcpr version=30204
#
# [2566] Maximum Difference by Remapping a Digit
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        min_num = num_str.replace(num_str[0], '0')
        max_num = num_str.replace(num_str[0], '9')
        if num_str[0] == '9':
            # try to find first non-9 digit
            for i in range(1, len(num_str)):
                if num_str[i] != '9':
                    max_num = num_str.replace(num_str[i], '9')
                    break
        return int(max_num) - int(min_num)
# @lc code=end



#
# @lcpr case=start
# 11891\n
# @lcpr case=end

# @lcpr case=start
# 90\n
# @lcpr case=end

#


#
# @lc app=leetcode id=1513 lang=python3
# @lcpr version=30204
#
# [1513] Number of Substrings With Only 1s
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
MOD = 10 ** 9 + 7
class Solution:
    def numSub(self, s: str) -> int:
        left = 0
        ans = 0
        while left < len(s):
            left_char = s[left]
            match left_char:
                case '0':
                    left += 1
                case '1':
                    right = left
                    while right < len(s) and s[right] == '1':
                        right += 1
                    length = right - left
                    ans += (length * (length + 1) // 2) % MOD
                    left = right
                    
        return ans % MOD
# @lc code=end



#
# @lcpr case=start
# "0110111"\n
# @lcpr case=end

# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "111111"\n
# @lcpr case=end

#


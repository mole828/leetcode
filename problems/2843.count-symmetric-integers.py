#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0
        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) % 2 == 0:
                left = num_str[:len(num_str) // 2]
                right = num_str[len(num_str) // 2:]
                if sum(map(ord, left)) == sum(map(ord, right)):
                    total += 1

        return total
        
# @lc code=end

print(Solution().countSymmetricIntegers(1200, 1230))
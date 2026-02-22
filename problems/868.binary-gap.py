#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        last = -1
        max_gap = 0
        for c in b:
            last += 1
            if c == '1':
                max_gap = max(max_gap, last)
                last = 0
            print(last, max_gap)
        return max_gap

# @lc code=end

if __name__ == '__main__':
    print(Solution().binaryGap(8))
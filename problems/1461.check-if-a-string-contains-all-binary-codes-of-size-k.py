#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        times = 2 ** k
        # if len(s) < k + times - 1:
        #     return False
        status = 0
        for left in range(len(s)-k+1):
            right = left+k
            sub = s[left:right]
            num = int(sub, base=2)
            this_status = 1 << num
            status |= this_status
            # print(sub, status)
        # print(bin(status), times)
        return bin(status).count('1') == times
# @lc code=end

if __name__ == '__main__':
    # left = 1 << (2**20)
    # print(left)
    # print(Solution().hasAllCodes("00110110", 2))
    print(Solution().hasAllCodes("00110", 2))
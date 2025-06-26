#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#

# @lc code=start

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n, m = len(s), k.bit_length()
        if n < m:
            return n
        ans = m if int(s[-m:], 2) <= k else m - 1
        return ans + s[:-m].count('0')


# @lc code=end

print(Solution().longestSubsequence("00101001", 1))
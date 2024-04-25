#
# @lc app=leetcode id=2370 lang=python3
# @lcpr version=
#
# [2370] Longest Ideal Subsequence
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# Time Limit Exceeded, 23 / 85 testcases passed
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        length = len(s)
        longest_sub = ''
        def dp(sub: str, i: int):
            # print(sub)
            if i == length:
                nonlocal longest_sub
                if len(sub) > len(longest_sub):
                    longest_sub = sub
                return
            dp(sub,i+1)
            c = s[i]
            if (sub and abs(ord(sub[-1]) - ord(c))<=k) or not sub:
                dp(sub+c, i+1)
        dp('',0)
        return len(longest_sub)

import numpy as np

# Memory Limit Exceeded, 71 / 85 testcases passed
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        array = np.array([ord(c) for c in s])
        diff_matrix = np.abs(array[:,np.newaxis] - array[np.newaxis,:])
        print(diff_matrix.size)
        dp = [0] * len(array)
        for i in range(len(array)-1, -1, -1):
            diff_row = diff_matrix[i][i+1:]
            next_step = np.where(diff_row<=k)[0] + (i + 1)
            next_iter = (dp[j] for j in next_step)
            dp[i] = max(next_iter,default=0) + 1
        return max(dp)

# Time Limit Exceeded, 73/85 cases passed
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        array = np.array([ord(c) for c in s])
        dp = np.array([0]*len(array))
        for i in range(len(array)-1,-1,-1):
            x = array[i]
            row = array[i+1:]
            diff_row = np.abs(row - x)
            next_step = np.where(diff_row<=k)[0] + (i+1)
            dp[i] = max([dp[j] for j in next_step],default=0) + 1
            # print(diff_row)
        return np.max(dp)


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        array = np.array([ord(c) for c in s])
        l = np.zeros(128, dtype=int)
        for c in array:
            l[c] = l[c-k:c+k+1].max() + 1
        return l.max()

# @lc code=end

print(Solution().longestIdealString("acfgbd",2))
print(Solution().longestIdealString("pvjcci",4))

#
# @lcpr case=start
# "acfgbd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n3\n
# @lcpr case=end

#


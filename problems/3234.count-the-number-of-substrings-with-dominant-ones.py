#
# @lc app=leetcode id=3234 lang=python3
# @lcpr version=30204
#
# [3234] Count the Number of Substrings With Dominant Ones
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0]
        arr = [int(c) for c in s]
        res = 0
        for left in range(len(arr)):
            for right in range(left, len(arr)):
                count[arr[right]] += 1
                if count[1] >= count[0] ** 2:
                    res += 1
            count = [0, 0]
        return res

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos0 = [-1] 
        total1 = 0 
        ans = 0

        for r, ch in enumerate(s):
            if ch == '0':
                pos0.append(r)
            else:
                total1 += 1
                ans += r - pos0[-1]

            for i in range(len(pos0) - 1, 0, -1):
                cnt0 = len(pos0) - i
                if cnt0 * cnt0 > total1:
                    break
                p, q = pos0[i - 1], pos0[i]
                cnt1 = r - q + 1 - cnt0 
                ans += max(q - max(cnt0 * cnt0 - cnt1, 0) - p, 0)
        return ans


# @lc code=end

print(Solution().numberOfSubstrings("00011"))

#
# @lcpr case=start
# "00011"\n
# @lcpr case=end

# @lcpr case=start
# "101101"\n
# @lcpr case=end

#


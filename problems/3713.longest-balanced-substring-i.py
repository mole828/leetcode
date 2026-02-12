#
# @lc app=leetcode id=3713 lang=python3
#
# [3713] Longest Balanced Substring I
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 1
        n = len(s)
        for length in range(n, 0, -1):
            for left in range(0, n - length + 1):
                sub = s[left : left + length]
                count = Counter(sub)
                c_set = set(v for v in count.values())
                # print(sub, count, c_set)
                if len(c_set) == 1:
                    ans = max(ans, length)
                    break
        return ans
    
class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestBalanced("abbac"))
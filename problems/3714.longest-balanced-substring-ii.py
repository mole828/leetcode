#
# @lc app=leetcode id=3714 lang=python3
#
# [3714] Longest Balanced Substring II
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
    
class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        ord_a = ord("a")
        set_0 = set([0])
        for i in range(n):
            cnt = [0] * 3
            for j in range(i, n):
                cnt[ord(s[j]) - ord_a] += 1
                if len(set(cnt)-set_0) == 1:
                    ans = max(ans, j - i + 1)
        return ans
    
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # 一种字母
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)

        # 两种字母
        def f(x: str, y: str) -> None:
            nonlocal ans
            i = 0
            while i < n:
                pos = {0: i - 1}  # 前缀和数组的首项是 0，位置相当于在 i-1
                d = 0  # x 的个数减去 y 的个数
                while i < n and (s[i] == x or s[i] == y):
                    d += 1 if s[i] == x else -1
                    if d in pos:
                        ans = max(ans, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
                i += 1

        f('a', 'b')
        f('a', 'c')
        f('b', 'c')

        # 三种字母
        # 前缀和数组的首项是 0，位置相当于在 -1
        pos = {(0, 0): -1}
        cnt = defaultdict(int)
        for i, b in enumerate(s):
            cnt[b] += 1
            p = (cnt['a'] - cnt['b'], cnt['b'] - cnt['c'])
            if p in pos:
                ans = max(ans, i - pos[p])
            else:
                pos[p] = i
        return ans



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestBalanced("abbac"))
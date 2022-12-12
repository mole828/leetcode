from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            g = Counter()
            for j in range(i, n):
                g[s[j]] += 1
                lst = g.values()
                ans += max(lst) - min(lst)
        return ans

if __name__ == '__main__':
    Solution().beautySum('aabcb')
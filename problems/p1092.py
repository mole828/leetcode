from functools import cache

'''
todo
'''

class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        # 这里在最后加个标志位，以便于s,t的公共子序列覆盖到s和t的最后一位
        # 方便下面计算答案
        s += '0'
        t += '0'
        n, m = len(s), len(t)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return ''
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + s[i]
            else:
                p, q = dfs(i - 1, j), dfs(i, j - 1)
                return p if len(p) > len(q) else  q
        # 最长公共子序列
        w = dfs(n - 1, m - 1)

        ans = []
        i = j = 0
        for x in w:
            while t[j] != x:
                ans.append(t[j])
                j += 1
            while s[i] != x:
                ans.append(s[i])
                i += 1
            ans.append(x)
            i += 1
            j += 1
        ans.pop()   # 将之前加入的0弹出去
        return ''.join(ans) # 这里直接返回ans也可以 小bug 哈哈

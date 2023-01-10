class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(map(str, list(range(k))))
        target = n + k ** n - 1
        ans = ''
        seen = set()
        def dfs(cur):
            nonlocal ans
            if len(cur) == target:
                ans = cur[:]
                return
            pre = cur[1 - n:]
            for i in range(k):
                tmp = pre + str(i)
                if tmp not in seen:
                    seen.add(tmp)
                    dfs(cur + str(i))
                    seen.remove(tmp)
                    if len(ans) > 0:
                        return
        dfs('')
        return ans
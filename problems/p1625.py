from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        t = list(s)
        q = deque([t])
        ans = s
        vis = {''.join(t)}
        
        def add(t):
            for i in range(len(t)):
                if i & 1:
                    t[i] = str((int(t[i]) + a) % 10)
            return t
        
        def move(t):
            n = len(t)
            return t[n - b:n] + t[:n - b]
        
        while q:
            cur = q.popleft()
            ans = min(ans,''.join(cur))
            nxt = cur
            nxta = add(nxt)
            nxtb = move(nxt)
            if (g := ''.join(nxta)) not in vis:
                vis.add(g)
                q.append(nxta)
            if (g := ''.join(nxtb)) not in vis:
                vis.add(g)
                q.append(nxtb)
        return ans
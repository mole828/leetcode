class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = [str(ord(c)-96) for c in s]
        ans = ''.join(ans)
        for i in range(k):
            ans = str(ans)
            ans = sum(int(c) for c in ans)
        return ans
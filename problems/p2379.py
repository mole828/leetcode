class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = w = sum([1 for _ in blocks[:k] if _ == 'W'])
        for right in range(k, n):
            w -= (blocks[right - k] == 'W')
            w += (blocks[right] == 'W')
            ans = min(ans, w)
        return ans